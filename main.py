from rich import print
import logging

from whisper_worker import Settings, RecordingDevice, WhisperWorker
from whisper_worker.transcription import TranscriptionResult


def transcription_callback(text: str, result: TranscriptionResult) -> None:
    print(result)


def main():
    settings = Settings.load("settings.yaml")
    logging.info("Using settings: ")
    logging.info(settings)

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    print(settings)
    recording_device = RecordingDevice(settings.mic_settings)
    whisper_worker = WhisperWorker(
        settings.whisper_worker,
        recording_device,
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    whisper_worker.listen(transcription_callback)


if __name__ == "__main__":
    main()
