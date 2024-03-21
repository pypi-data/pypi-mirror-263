# Author: Yiannis Charalambous

from typing import Literal, overload
from typing_extensions import override

from pyautoconfig import JsonTypes, JsonConfigNode


class TemplateConfigNode(JsonConfigNode):
    """`TemplateConfigNode` checks that the children fit into the template.
    For dictionaries, it relaxes the constraints that check if the
    `key:value` in a dictionary match the specification in the `json_node`.
    Instead, the values are only checked, and the keys are allowed to be any
    value. This allows for objects to have an arbitrary amount of fields inside
    that have the same structure, but are named differently.

    In short: Allows to include fields inside an object with an arbitrary name.
    The values are defined using a template and each object is checked to see if
    it matches."""

    @override
    def __init__(
        self,
        node_type: Literal["list", "dict"],
        default_value: JsonTypes = "",
        is_optional: bool = False,
        _name: str = "",
    ) -> None:
        """The following fields are redefined for the dataclass:
        * default_value - The template used for each field.
        * is_optional - If the node needs to be defined, same as `JsonConfigNode`."""

        self.node_type: Literal["list", "dict"] = node_type

        super().__init__(
            default_value,
            is_optional=is_optional,
            show_in_config=False,
            _name=_name,
        )

    @override
    @classmethod
    def _init_node_from_default(cls, node: JsonConfigNode) -> JsonTypes:
        if not isinstance(node, "TemplateConfigNode"):
            return super()._init_node_from_default(node)
        # Return empty.
        if node.node_type is "list":
            return []
        elif node.node_type is "dict":
            return {}
        else:
            raise ValueError(f"{node._name} is not a valid node_type: {node.node_type}")

    @override
    def _init_child_fields(self, recursively: bool = False) -> None:
        # Nothing to initialize in the schema (_name does not apply to default_value as it is
        # used as a template)
        pass

    @override
    def init_node_value(
        self,
        json_node: JsonTypes,
        create_missing_fields: bool = True,
    ) -> JsonTypes:
        # The super method tests the json_node against the default_value set against this
        # object, so if we iterate and call the super method against the json_node of the
        # children, then it should automatically perform the checks required onto the children.

        assert isinstance(
            json_node, dict | list
        ), f"The JsonNode supplied to {self._name} must be a list or a dictionary."

        if isinstance(json_node, list) and self.node_type is "list":
            result_list: list[JsonTypes] = []
            for child in json_node:
                node_value: JsonTypes = super().init_node_value(
                    json_node=child, create_missing_fields=create_missing_fields
                )
                result_list.append(node_value)
            return result_list
        elif isinstance(json_node, dict) and self.node_type is "dict":
            result: dict[str, JsonTypes] = {}
            for key, value in json_node.items():
                node_value: JsonTypes = super().init_node_value(
                    json_node=value, create_missing_fields=create_missing_fields
                )
                result[key] = node_value
            return result
        else:
            raise ValueError(f"{self._name} has an invalid node_type {self.node_type}")
