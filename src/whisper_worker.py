from dataclasses import dataclass
import os
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

from src import Settings, Mic


@dataclass
class TranscriptionResult:
    text: str
    segments: list
    language: str


class WhisperWorker:
    def __init__(self, args: Settings):
        # Load / Download model
        self._model = args.model
        if args.model != "large" and not args.non_english:
            model = self._model + ".en"
        self.audio_model = whisper.load_model(model)

        # Thread safe Queue for passing data from the threaded recording callback.
        self.data_queue = Queue()
        self.args = args

        self.transcription = [""]
        self.phrase_time = None

    def transcribe(self, audio_np: np.ndarray) -> TranscriptionResult:
        result = self.audio_model.transcribe(
            # TODO: Could add more settings here.
            audio_np,
            fp16=torch.cuda.is_available(),
        )

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
            seconds=self.args.phrase_timeout
        )
