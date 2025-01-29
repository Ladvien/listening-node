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
from src.whisper_worker import WhisperWorker


def main():
    args = Settings.load("settings.yaml")
    print("Using settings: ")
    print(args)
    input("Press a key to continue...")

    # The last time a recording was retrieved from the queue.
    phrase_time = None

    # We use SpeechRecognizer to record our audio because it has a nice feature where it can detect when speech ends.
    recorder = sr.Recognizer()

    # TODO: Could add more settings here.
    recorder.energy_threshold = args.energy_threshold

    # Definitely do this, dynamic energy compensation lowers the energy threshold dramatically to a point where the SpeechRecognizer never stops recording.
    recorder.dynamic_energy_threshold = False

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    mic = Mic(settings=args.mic_settings)

    whisper_worker = WhisperWorker(args)

    transcription = [""]

    with mic.source:
        recorder.adjust_for_ambient_noise(mic.source)

    def record_callback(_, audio: sr.AudioData) -> None:
        """
        Threaded callback function to receive audio data when recordings finish.
        audio: An AudioData containing the recorded bytes.
        """
        # Grab the raw bytes and push it into the thread safe queue.
        data = audio.get_raw_data()
        whisper_worker.data_queue.put(data)

    # Create a background thread that will pass us raw audio bytes.
    # We could do this manually but SpeechRecognizer provides a nice helper.
    recorder.listen_in_background(
        mic.source, record_callback, phrase_time_limit=args.record_timeout
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    whisper_worker.listen()

    print("\n\nTranscription:")

    for line in transcription:
        print(line)


if __name__ == "__main__":
    main()
