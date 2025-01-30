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

from src import Settings
from src.recording_device import RecordingDevice
from src.whisper_worker import WhisperWorker


def main():
    args = Settings.load("settings.yaml")
    logging.info("Using settings: ")
    logging.info(args)

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    print(args)
    input("Press Enter to continue...")
    recording_device = RecordingDevice(args.mic_settings)
    whisper_worker = WhisperWorker(args, recording_device)

    transcription = [""]

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    whisper_worker.listen()

    print("\n\nTranscription:")

    for line in transcription:
        print(line)


if __name__ == "__main__":
    main()
