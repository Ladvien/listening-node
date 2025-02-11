from rich import print
import logging

from listening_node import Settings, RecordingDevice, ListeningNode
from listening_node.transcription import TranscriptionResult


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
    listening_node = ListeningNode(
        settings.listening_node,
        recording_device,
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    listening_node.listen(transcription_callback)


if __name__ == "__main__":
    main()
