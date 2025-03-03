from rich import print
import logging

from listening_tool import Config, RecordingDevice, ListeningTool
from listening_tool.transcription import TranscriptionResult


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
    listening_tool = ListeningTool(
        config.listening_tool,
        recording_device,
    )

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    listening_tool.listen(transcription_callback)


if __name__ == "__main__":
    main()
