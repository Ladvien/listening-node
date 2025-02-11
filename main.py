from rich import print
import logging

from listening_node import Config, RecordingDevice, ListeningNode
from listening_node.transcription import TranscriptionResult


def transcription_callback(text: str, result: TranscriptionResult) -> None:
    print(result)


def main():
    config = Config.load("config.yaml")
    logging.info("Using config: ")
    logging.info(config)

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    print(config)
    recording_device = RecordingDevice(config.mic_config)
    listening_node = ListeningNode(
        config.listening_node,
        recording_device,
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    listening_node.listen(transcription_callback)


if __name__ == "__main__":
    main()
