from rich import print
import logging

from src import Settings
from src.recording_device import RecordingDevice
from src.whisper_worker import WhisperWorker


def transcription_callback(text: str, result: dict) -> None:
    print(result)


def main():
    args = Settings.load("settings.yaml")
    logging.info("Using settings: ")
    logging.info(args)

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    print(args)
    recording_device = RecordingDevice(args.mic_settings)
    whisper_worker = WhisperWorker(
        args.whisper_worker,
        recording_device,
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    whisper_worker.listen(transcription_callback)


if __name__ == "__main__":
    main()
