from json import load
from typing import Type, TypeVar

ConfigType = TypeVar("ConfigType")


def load_config(config_file_path: str, config_type: Type[ConfigType]) -> ConfigType:
    with open(config_file_path) as file:
        return config_type(**load(file))
