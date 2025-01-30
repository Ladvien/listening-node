from dataclasses import dataclass, asdict
from ast import literal_eval
import os
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
import numpy as np
import speech_recognition as sr
import whisper
import torch
from rich import print
import logging
from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform
from whisper.model import Whisper

from src.recording_device import RecordingDevice


@dataclass
class TranscriptionResult:
    text: str
    segments: list
    language: str


@dataclass
class TranscribeSettings:
    """
      transcribe_settings:
    #  'tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo'
    model: medium

    # Whether to display the text being decoded to the console. If True, displays all the details, If False, displays minimal details. If None, does not display anything
    verbose: False

    # Temperature for sampling. It can be a tuple of temperatures,
    # which will be successively used upon failures according to
    # either compression_ratio_threshold or logprob_threshold.
    temperature: "(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)" # "(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)"

    # If the gzip compression ratio is above this value,
    # treat as failed
    compression_ratio_threshold: 2.4 # 2.4

    # If the average log probability over sampled tokens is below this value, treat as failed
    logprob_threshold: -1.0 # -1.0

    # If the no_speech probability is higher than this value AND
    # the average log probability over sampled tokens is below
    # logprob_threshold, consider the segment as silent
    no_speech_threshold: 0.6 # 0.6

    # if True, the previous output of the model is provided as a
    # prompt for the next window; disabling may make the text
    # inconsistent across windows, but the model becomes less
    # prone to getting stuck in a failure loop, such as repetition
    # looping or timestamps going out of sync.
    condition_on_previous_text: True # True

    # Extract word-level timestamps using the cross-attention
    # pattern and dynamic time warping, and include the timestamps
    # for each word in each segment.
    word_timestamps: False # False

    # If word_timestamps is True, merge these punctuation symbols
    # with the next word
    prepend_punctuations: >
      "\"'“¿([{-"

    # If word_timestamps is True, merge these punctuation symbols with the previous word
    append_punctuations: >
      "\"'.。,，!！?？:：”)]}、"

    # Optional text to provide as a prompt for the first window.
    # This can be used to provide, or "prompt-engineer" a context
    # for transcription, e.g. custom vocabularies or proper nouns
    # to make it more likely to predict those word correctly.
    initial_prompt: "" # ""

    # Keyword arguments to construct DecodingOptions instances
    decode_options: dict

    # Comma-separated list start,end,start,end,... timestamps
    # (in seconds) of clips to process. The last end timestamp
    # defaults to the end of the file.
    clip_timestamps: Union[str, List[float]]

    # When word_timestamps is True, skip silent periods longer
    # than this threshold (in seconds) when a possible
    # hallucination is detected
    hallucination_silence_threshold: ""
    """

    model: str
    verbose: bool
    temperature: Union[float, Tuple[float, ...]]
    compression_ratio_threshold: float
    logprob_threshold: float
    no_speech_threshold: float
    condition_on_previous_text: bool
    word_timestamps: bool
    prepend_punctuations: str
    append_punctuations: str
    initial_prompt: Optional[str]
    clip_timestamps: Union[str, List[float]]
    hallucination_silence_threshold: Optional[float]

    @classmethod
    def load(cls, data):
        return cls(**data)

    def __post_init__(self):
        if isinstance(self.temperature, str):
            self.temperature = literal_eval(self.temperature)
        if isinstance(self.clip_timestamps, str):
            if "," in self.clip_timestamps:
                values = self.clip_timestamps.split(",")
                self.clip_timestamps = (float(v) for v in values)

    def to_dict(self):
        return asdict(self)


class WhisperWorker:
    # TODO: def __init__(self, args: WhisperWorkerSettings, recording_device: RecordingDevice) -> None:
    def __init__(self, settings: Any, recording_device: RecordingDevice) -> None:

        self.settings = settings
        self.recording_device = recording_device
        self.recorder = sr.Recognizer()

        # Load / Download model
        print(f"Loading model: {self.settings.transcribe_settings.model}")
        self.audio_model = whisper.load_model(self.settings.transcribe_settings.model)

        # Thread safe Queue for passing data from the threaded recording callback.
        self.data_queue = Queue()

        self.transcription = [""]
        self.phrase_time = None

        # Create a background thread that will pass us raw audio bytes.
        # We could do this manually but SpeechRecognizer provides a nice helper.
        def record_callback(_, audio: sr.AudioData) -> None:
            """
            Threaded callback function to receive audio data when recordings finish.
            audio: An AudioData containing the recorded bytes.
            """
            # Grab the raw bytes and push it into the thread safe queue.
            data = audio.get_raw_data()
            self.data_queue.put(data)

        self.recording_device.recorder.listen_in_background(
            self.recording_device.mic.source,
            record_callback,
            phrase_time_limit=self.settings.record_timeout,
        )

    def transcribe(self, audio_np: np.ndarray) -> TranscriptionResult:
        start_time = datetime.now()
        settings = self.settings.transcribe_settings.to_dict()
        del settings["model"]
        result = self.audio_model.transcribe(
            audio_np,
            fp16=torch.cuda.is_available(),
            **settings,
        )
        logging.info(f"Transcription took: {datetime.now() - start_time} seconds.")

        return TranscriptionResult(
            text=result["text"].strip(),
            segments=result["segments"],
            language=result["language"],
        )

    def listen(self, callback: Optional[Callable[[str, Dict], None]] = None) -> None:
        while True:
            try:
                now = datetime.now(datetime.now().astimezone().tzinfo)

                # Pull raw recorded audio from the queue.
                if not self.data_queue.empty():

                    phrase_complete = False

                    # If enough time has passed between recordings, consider the phrase complete.
                    # Clear the current working audio buffer to start over with the new data.
                    if self._phrase_complete(self.phrase_time, now):
                        phrase_complete = True

                    # This is the last time we received new audio data from the queue.
                    self.phrase_time = now

                    # Combine audio data from queue
                    audio_data = b"".join(self.data_queue.queue)
                    self.data_queue.queue.clear()

                    # Convert in-ram buffer to something the model can use directly without needing a temp file.
                    # Convert data from 16 bit wide integers to floating point with a width of 32 bits.
                    # Clamp the audio stream frequency to a PCM wavelength compatible default of 32768hz max.
                    audio_np = (
                        np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)
                        / 32768.0
                    )

                    # Read the transcription.
                    result = self.transcribe(audio_np)

                    # If we detected a pause between recordings, add a new item to our transcription.
                    # Otherwise edit the existing one.
                    if phrase_complete:
                        self.transcription.append(result.text)
                    else:
                        self.transcription[-1] = result.text

                    # Clear the console to reprint the updated transcription.
                    # os.system("cls" if os.name == "nt" else "clear")
                    for line in self.transcription:
                        logging.info(line)

                    if callback:
                        callback(self.transcription, result)
                else:
                    # Infinite loops are bad for processors, must sleep.
                    sleep(0.25)
            except KeyboardInterrupt:
                break

    def _phrase_complete(self, phrase_time: datetime, now: datetime) -> bool:

        return phrase_time and now - phrase_time > timedelta(
            seconds=self.settings.phrase_timeout
        )
