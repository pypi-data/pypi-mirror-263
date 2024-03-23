# Author: Yiannis Charalambous

from typing import Any
from pyautoconfig import JsonTypes


class JsonConfigNode(object):
    def __init__(
        self,
        default_value: JsonTypes = "",
        is_optional: bool = False,
        show_in_config: bool = True,
        _name: str | int = "",
    ) -> None:
        """Is a description of how a Json structure will be defined. Currently, it does not support
        updating the schema, so the value passed as `default_value` is immutable.

        Args:
            default_value - Should be a BaseJsonTypes, JsonTypes. If it is a dict, then the
            key should be string, as specified in the Json spec. The value should be a `JsonConfigNode`.

            is_optional - Will not load the config if the value is not specified by the user. If
            true will assign default_value.

            show_in_config - Show this field in the config tool UI."""
        self._default_value: JsonTypes = default_value
        self.is_optional: bool = is_optional
        self.show_in_config: bool = show_in_config
        self._name = _name

        # Init already added children.
        self._init_child_fields()

    @property
    def default_value(self) -> JsonTypes:
        return self._default_value

    @classmethod
    def _init_node_from_default(cls, node: "JsonConfigNode") -> JsonTypes:
        """Recursively builds a json struct and returns it from the JsonConfigNode"""
        if isinstance(node.default_value, dict):
            values: dict = {}
            for key, value in node.default_value.items():
                values[key] = cls._init_node_from_default(value)
            return values
        elif isinstance(node.default_value, list):
            # FIXME Not supported currently, maybe this should be kept like this as it would return
            # an array of the schema.
            return node.default_value
        else:
            return node.default_value

    def _init_child_fields(self, recursively: bool = False) -> None:
        """Initializes `_name` field of `JsonConfigNode`."""
        if isinstance(self.default_value, dict):
            for key, child_node in self.default_value.items():
                # Init fields.
                assert isinstance(
                    child_node, JsonConfigNode
                ), f"The node '{key}' child of {self._name} is not a JsonConfigNode."
                child_node._name = key
                if recursively:
                    child_node._init_child_fields(recursively)
        elif isinstance(self.default_value, list):
            for idx, child_node in enumerate(self.default_value):
                # Init elements
                assert isinstance(
                    child_node, JsonConfigNode
                ), f"The child of {self._name} at index {idx} is not a JsonConfigNode."
                child_node._name = idx
                if recursively:
                    child_node._init_child_fields(recursively)

    def __getitem__(self, path: Any):
        """Indexing the JsonConfigNode will directly access the default_value
        child if it is a `dict` or a `list`."""

        # Need to dynamically resolve type.
        path_list: list[int | str]
        if isinstance(path, str | int):
            path_list = [path]
        elif isinstance(path, tuple):
            path_list = list(path)
        else:
            raise TypeError(
                f"{path} is not an int, str or tuple of those types: {type(path)}"
            )

        current_value: JsonConfigNode = self
        for path_element in path_list:
            if isinstance(current_value.default_value, dict):
                current_value = current_value.default_value[path_element]
            elif isinstance(current_value.default_value, list) and isinstance(
                path_element, int
            ):
                current_value = current_value.default_value[path_element]
            else:
                raise IndexError(f"Invalid access {path_element} from {path}")
        return current_value

    def init_node_value(
        self,
        json_node: JsonTypes,
        create_missing_fields: bool = True,
    ) -> JsonTypes:
        """Initializes recursively the json nodes based on the template described in
        JsonConfigNode. This class specifically implements all the base types supported
        by Json as described by `JsonTypes`."""
        node = self
        # Check if types match, if not then initialize to proper type if
        # allowed.
        if type(node.default_value) is not type(json_node):
            # Initialize default field if allowed.
            if create_missing_fields or node.is_optional:
                return self._init_node_from_default(node)
            else:
                raise ValueError(
                    f"JsonConfigLoader Error: {node._name} is not of type: "
                    f"{type(node.default_value)}, instead is {type(json_node)}"
                )
        # Check if list.
        elif isinstance(node.default_value, list):
            # FIXME Lists not supported so they are not touched.
            return json_node
        # Recursive case: Check if type is object
        elif isinstance(node.default_value, dict):
            assert isinstance(json_node, dict)
            for name, child in node.default_value.items():
                # Check each element of object.
                # If node does not exist then create.
                if name in json_node:
                    json_node[name] = child.init_node_value(
                        json_node=json_node[name],
                        create_missing_fields=create_missing_fields,
                    )
                elif create_missing_fields or node.is_optional:
                    json_node[name] = self._init_node_from_default(child)
                else:
                    raise ValueError(
                        f"JsonConfigLoader Error: {node._name} is not of type: "
                        f"{type(node.default_value)}, instead is {type(json_node)}"
                    )
            return json_node
        # Is primitive type so just return
        else:
            return json_node
