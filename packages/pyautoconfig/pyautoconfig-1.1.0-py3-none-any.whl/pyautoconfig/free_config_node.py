# Author: Yiannis Charalambous

from typing_extensions import override
from config_loader import JsonTypes, JsonConfigNode


class FreeConfigNode(JsonConfigNode):
    """`FreeConfigNode` will not check children if they conform to the sprcification. The following
    fields are interpreted like so:

    Args:
        * default_value - Will be used when creating a default value, so it should probably be empty
        or contain default data that is going to be initialized. **The data passed to it should not be
        JsonConfigNode objects, but JsonTypes.**"""

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
        return node.default_value

    @override
    def _init_children(self) -> None:
        return

    @override
    def init_node_value(
        self,
        json_node: JsonTypes,
        create_missing_fields: bool = True,
    ) -> JsonTypes:
        return json_node
