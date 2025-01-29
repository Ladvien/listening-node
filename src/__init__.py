from sys import platform
import rich
import yaml
from dataclasses import dataclass
import speech_recognition
import logging


@dataclass
class MicSettings:
    mic_name: str
    sample_rate: int

    @classmethod
    def load(cls, data):
        return cls(**data)


@dataclass
class Mic:
    settings: MicSettings
    source: speech_recognition.Microphone | None = None

    def __post_init__(self):
        if "linux" in platform:
            print("Available microphone devices are: ")
            for index, name in enumerate(
                speech_recognition.Microphone.list_microphone_names()
            ):
                print(f'Microphone with name "{name}" found')

            for index, name in enumerate(
                speech_recognition.Microphone.list_microphone_names()
            ):
                if self.settings.mic_name in name:
                    self.source = speech_recognition.Microphone(
                        sample_rate=self.settings.sample_rate, device_index=index
                    )
                    print(f"Found target mic: '{self.settings.mic_name}'")
                    break

        else:
            self.source = speech_recognition.Microphone(
                sample_rate=self.settings.sample_rate
            )


@dataclass
class LoggingConfig:
    level: int
    filepath: str
    log_entry_format: str
    date_format: str

    def __post_init__(self):
        level = getattr(logging, self.level.upper())
        logging.basicConfig(
            filename=self.filepath,
            format=self.log_entry_format,
            level=level,
            datefmt=self.date_format,
        )


@dataclass
class Settings:
    model: str
    non_english: bool
    energy_threshold: int
    record_timeout: float
    phrase_timeout: float
    mic_settings: MicSettings
    logging_config: LoggingConfig

    @classmethod
    def load(cls, path):
        with open(path, "r") as f:
            data = yaml.safe_load(f)
            print(f"Loaded settings from {path}")
            print(data)
        return cls(**data)

    def __post_init__(self):
        self.mic_settings = MicSettings.load(self.mic_settings)
        self.logging_config = LoggingConfig(**self.logging_config)
