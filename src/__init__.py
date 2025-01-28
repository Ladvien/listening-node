import rich
import yaml
from dataclasses import dataclass


@dataclass
class Settings:
    mic_name: str
    model: str
    non_english: bool
    energy_threshold: int
    record_timeout: float
    phrase_timeout: float
    default_microphone: str

    @classmethod
    def load(cls, path):
        with open(path, "r") as f:
            data = yaml.safe_load(f)
            print(f"Loaded settings from {path}")
            print(data)
        return cls(**data)
