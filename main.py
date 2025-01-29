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
from src.recording_device import RecordingDevice
from src.whisper_worker import WhisperWorker


def main():
    args = Settings.load("settings.yaml")
    print("Using settings: ")
    print(args)
    input("Press a key to continue...")

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone

    recording_device = RecordingDevice(args)
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
