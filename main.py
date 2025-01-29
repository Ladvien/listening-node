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

    # Thread safe Queue for passing data from the threaded recording callback.
    data_queue = Queue()

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
        data_queue.put(data)

    # Create a background thread that will pass us raw audio bytes.
    # We could do this manually but SpeechRecognizer provides a nice helper.
    recorder.listen_in_background(
        mic.source, record_callback, phrase_time_limit=args.record_timeout
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")

    while True:
        try:
            now = datetime.now(datetime.now().astimezone().tzinfo)

            # Pull raw recorded audio from the queue.
            if not data_queue.empty():

                phrase_complete = False
                # If enough time has passed between recordings, consider the phrase complete.
                # Clear the current working audio buffer to start over with the new data.
                if phrase_time and now - phrase_time > timedelta(
                    seconds=args.phrase_timeout
                ):
                    phrase_complete = True

                # This is the last time we received new audio data from the queue.
                phrase_time = now

                # Combine audio data from queue
                audio_data = b"".join(data_queue.queue)
                data_queue.queue.clear()

                # Convert in-ram buffer to something the model can use directly without needing a temp file.
                # Convert data from 16 bit wide integers to floating point with a width of 32 bits.
                # Clamp the audio stream frequency to a PCM wavelength compatible default of 32768hz max.
                audio_np = (
                    np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)
                    / 32768.0
                )

                # Read the transcription.
                result = whisper_worker.transcribe(audio_np)

                # If we detected a pause between recordings, add a new item to our transcription.
                # Otherwise edit the existing one.
                if phrase_complete:
                    transcription.append(result.text)
                else:
                    transcription[-1] = result.text

                # Clear the console to reprint the updated transcription.
                os.system("cls" if os.name == "nt" else "clear")
                for line in transcription:
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

    print("\n\nTranscription:")

    for line in transcription:
        print(line)


if __name__ == "__main__":
    main()
