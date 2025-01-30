from dataclasses import asdict, dataclass

import yaml
from .mic import MicSettings, Mic
from .logging_config import LoggingConfig
from .whisper_worker import TranscribeSettings


@dataclass
class WhisperWorkerSettings:
    record_timeout: float
    phrase_timeout: float
    transcribe_settings: TranscribeSettings

    @classmethod
    def load(cls, data):
        return cls(**data)

    def __post_init__(self):
        self.transcribe_settings = TranscribeSettings.load(self.transcribe_settings)


@dataclass
class Settings:
    whisper_worker: WhisperWorkerSettings
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
        self.whisper_worker = WhisperWorkerSettings.load(self.whisper_worker)
        self.mic_settings = MicSettings.load(self.mic_settings)
        self.logging_config = LoggingConfig(**self.logging_config)
