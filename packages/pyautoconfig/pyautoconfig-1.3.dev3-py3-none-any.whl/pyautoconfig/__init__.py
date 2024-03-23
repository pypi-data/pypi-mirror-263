# Author: Yiannis Charalambous

# Define base types that all imports use.
EnvTypes = bool | float | int | str
JsonBaseTypes = bool | float | int | str
"""Contains a list of primitive Json value types."""
JsonTypes = JsonBaseTypes | list | dict
"""Contains an extended type definition that includes composite data types
like lists."""

from .base_config_loader import BaseConfigLoader
from .env_config_loader import EnvConfigLoader, EnvConfigField
from .json_config_loader import JsonConfigLoader
from .json_config_node import JsonConfigNode

__all__ = [
    "JsonTypes",
    "BaseConfigLoader",
    "EnvConfigField",
    "EnvConfigLoader",
    "JsonConfigLoader",
    "JsonConfigNode",
]
