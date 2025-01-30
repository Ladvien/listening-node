from dataclasses import dataclass

import yaml
from .mic import MicSettings, Mic
from .logging_config import LoggingConfig
from .whisper_worker import ModelConfig


@dataclass
class Settings:
    # model: str
    model_size: str
    non_english: bool
    record_timeout: float
    phrase_timeout: float
    model_config: ModelConfig
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
        self.model_config = ModelConfig.load(self.model_config)
        self.mic_settings = MicSettings.load(self.mic_settings)
        self.logging_config = LoggingConfig(**self.logging_config)
