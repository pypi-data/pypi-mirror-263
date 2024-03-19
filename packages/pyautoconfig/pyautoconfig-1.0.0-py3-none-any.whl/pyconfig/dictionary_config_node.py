# Author: Yiannis Charalambous

from typing_extensions import override

from config_loader import JsonTypes, JsonConfigNode


class DictionaryConfigNode(JsonConfigNode):
    """`DictionaryConfigNode` relaxes the constraints that check if the
    `key:value` in a dictionary match the specification in the `json_node`.
    Instead, the values are only checked, and the keys are allowed to be any
    value. This allows for objects to have an arbitrary amount of fields inside
    that have the same structure, but are named differently.

    In short: Allows to include fields inside an object with an arbitrary name.
    The values are defined using a template and each object is checked to see if
    it matches.

    The following fields are redefined for the dataclass:
    * default_value - The template used for each field.
    * is_optional - Not used.
    * _name - Unused."""

    @override
    def __init__(
        self,
        default_value: JsonTypes = "",
        is_optional: bool = False,
        show_in_config: bool = True,
        _name: str = "",
    ) -> None:
        super().__init__(default_value, is_optional, show_in_config, _name)

        self.children: dict[str, JsonTypes] = {}

    @override
    @classmethod
    def _init_node_from_default(cls, node: JsonConfigNode) -> JsonTypes:
        raise NotImplementedError()

    @override
    def init_node_value(
        self,
        json_node: JsonTypes,
        create_missing_fields: bool = True,
    ) -> JsonTypes:
        raise NotImplementedError()
