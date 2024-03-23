# Author: Yiannis Charalambous

import os
import json
from typing import Optional
from typing_extensions import override

from pyautoconfig import JsonTypes
from .base_config_loader import BaseConfigLoader
from .json_config_node import JsonConfigNode

# TODO Write tests


class JsonConfigLoader(BaseConfigLoader):
    def __init__(
        self,
        content: Optional[str],
        root_node: JsonConfigNode,
        create_missing_fields: bool = False,
    ) -> None:

        self.root_node: JsonConfigNode = root_node
        assert isinstance(self.root_node.default_value, dict)

        super().__init__(
            content=content,
            create_missing_fields=create_missing_fields,
        )

    @classmethod
    def load_file(
        cls,
        file_path: str,
        root_node: JsonConfigNode,
        create_missing_fields: bool = False,
    ) -> "JsonConfigLoader":
        file_path = os.path.expanduser(os.path.expandvars(file_path))
        assert file_path.endswith(".json"), f"{file_path} is not a valid json file."

        content: Optional[str] = None
        # Read the file. If not possible then the rest will be handled in the
        # constructor.
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, "r") as file:
                content = file.read()
        else:
            raise FileNotFoundError(f"The file {file_path} is not found.")

        return JsonConfigLoader(
            content=content,
            root_node=root_node,
            create_missing_fields=create_missing_fields,
        )

    @classmethod
    def from_schema(cls, root_node: JsonConfigNode) -> "JsonConfigLoader":
        """Creates a loader from only schema."""
        return JsonConfigLoader(
            root_node=root_node,
            create_missing_fields=True,
            content=None,
        )

    @override
    def save(self, file_path: str) -> None:
        with open(file_path, "w") as f:
            json.dump(self.json_content, f)

    @override
    def _init_defaults(self) -> str:
        default_json: JsonTypes = JsonConfigNode._init_node_from_default(self.root_node)
        assert isinstance(default_json, dict)
        return json.dumps(default_json)

    def get_value(self, *path: str | int) -> JsonTypes:
        """Gets a value from the Json."""
        current_value: JsonTypes = self.json_content
        for element in path:
            if isinstance(current_value, dict):
                current_value = current_value[element]
            elif isinstance(current_value, list) and isinstance(element, int):
                current_value = current_value[element]
            else:
                raise IndexError(f"Invalid access {element} from {path}")
        return current_value

    def set_value(self, value: JsonTypes, *path: str | int) -> None:
        """Sets a value in the Json."""
        parent_path: tuple[int | str, ...] = path[:-1]
        parent_element = self.get_value(*parent_path)
        if isinstance(parent_element, list) and isinstance(path[-1], int):
            parent_element[path[-1]] = value
        elif isinstance(parent_element, dict):
            parent_element[path[-1]] = value
        else:
            raise IndexError(
                f"Invalid set value {value} of type {type(value)} "
                f"for {path[-1]} from {path}"
            )

    @override
    def _read_fields(self, create_missing_fields: bool = False) -> None:
        """Parses the JSON config and loads all the values recursively. The self.values should
        map directly to how the self.node values are laid out.

        Arg:
            create_missing_field: bool - Will not give an error when an invalid/missing field
            is encountered, will instead initialize it to the default value."""
        self.json_content: dict = json.loads(self.raw_content)

        # Start with root object.
        json_content: JsonTypes = self.root_node.init_node_value(
            json_node=self.json_content,
            create_missing_fields=create_missing_fields,
        )
        assert isinstance(json_content, dict)

        self.json_content = json_content
