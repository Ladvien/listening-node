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
