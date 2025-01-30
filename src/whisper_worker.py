from dataclasses import dataclass
import os
from typing import Any, Dict, List, Optional, Tuple, Union
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
class ModelConfig:
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
    decode_options: Dict
    clip_timestamps: Union[str, List[float]]
    hallucination_silence_threshold: Optional[float]

    @classmethod
    def load(cls, data):
        return cls(**data)


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
        result = self.audio_model.transcribe(
            # TODO: Could add more settings here.
            audio_np,
            fp16=torch.cuda.is_available(),
        )
        logging.info(f"Transcription took: {datetime.now() - start_time} seconds.")

        return TranscriptionResult(
            text=result["text"].strip(),
            segments=result["segments"],
            language=result["language"],
        )

    def listen(self):
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
                    os.system("cls" if os.name == "nt" else "clear")
                    for line in self.transcription:
                        logging.info(line)
                        print(f"[green]{line}[/green]")
                        # print(f"[red]{segments}[/red]")
                        # print(f"[blue]{language}[/blue]")
                    # Flush stdout.
                    print("", end="", flush=True)
                else:
                    # Infinite loops are bad for processors, must sleep.
                    sleep(0.25)
            except KeyboardInterrupt:
                break

    def _phrase_complete(self, phrase_time: datetime, now: datetime) -> bool:

        return phrase_time and now - phrase_time > timedelta(
            seconds=self.settings.phrase_timeout
        )
