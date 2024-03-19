# Author: Yiannis Charalambous

import json
from typing_extensions import override

from pyautoconfig import JsonTypes
from .base_config_loader import BaseConfigLoader
from .json_config_node import JsonConfigNode

# TODO Write tests


class JsonConfigLoader(BaseConfigLoader):
    def __init__(
        self,
        root_node: JsonConfigNode,
        file_path: str = "~/.config/esbmc-ai.json",
        create_missing_fields: bool = False,
    ) -> None:
        assert file_path.endswith(
            ".json"
        ), f"{self.file_path} is not a valid json file."

        self.root_node: JsonConfigNode = root_node
        assert isinstance(self.root_node.default_value, dict)

        super().__init__(
            file_path=file_path,
            create_missing_fields=create_missing_fields,
        )

    @override
    def save(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.json_content, f)

    @override
    def _create_default_file(self) -> None:
        default_json: JsonTypes = JsonConfigNode._init_node_from_default(self.root_node)
        assert isinstance(default_json, dict)
        with open(self.file_path, "w") as f:
            json.dump(default_json, f)

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
        self.json_content: dict = json.loads(self.content)

        # Start with root object.
        json_content: JsonTypes = self.root_node.init_node_value(
            json_node=self.json_content,
            create_missing_fields=create_missing_fields,
        )
        assert isinstance(json_content, dict)

        self.json_content = json_content
