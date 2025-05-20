from pathlib import Path
import yaml
import os
from src.models.AppConfig import AppConfig

CONFIG_PATH = Path(__file__).parent / "config.yaml"

def load_config(path: Path = CONFIG_PATH) -> AppConfig:
    with open(path, "r") as f:
        raw_yaml = f.read()

    expanded_yaml = os.path.expandvars(raw_yaml)

    raw_config = yaml.safe_load(expanded_yaml)

    return AppConfig(**raw_config)
