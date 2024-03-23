# Author: Yiannis Charalambous

import pytest

from pyautoconfig.json_config_node import JsonConfigNode


def test_init_child_and_access() -> None:
    # Tests if children have been init properly and also if accessing them is possible.

    root: JsonConfigNode = JsonConfigNode(
        {
            "option_1": JsonConfigNode("abc"),
            "option_2": JsonConfigNode(
                {
                    "option_2a": JsonConfigNode({"option_2aa": JsonConfigNode(1.0)}),
                    "option_2b": JsonConfigNode("qwerty"),
                }
            ),
            "option_3": JsonConfigNode(1.0),
        }
    )

    assert root["option_1"]._name == "option_1"
    assert root["option_2"]._name == "option_2"
    assert root["option_2", "option_2a"]._name == "option_2a"
    assert root["option_2", "option_2a", "option_2aa"]._name == "option_2aa"
    assert root["option_2", "option_2b"]._name == "option_2b"
    assert root["option_3"]._name == "option_3"


def test_list_access() -> None:
    root: JsonConfigNode = JsonConfigNode(
        {
            "child": JsonConfigNode(
                [
                    JsonConfigNode("qwer"),
                    JsonConfigNode(1),
                    JsonConfigNode({"child2": JsonConfigNode("asdfg")}),
                ]
            ),
        }
    )

    assert root["child"]._name == "child"
    assert root["child", 0]._name == 0
    assert root["child", 1]._name == 1
    assert root["child", 2]._name == 2
    assert root["child", 2, "child2"]._name == "child2"


def test_init_node_value() -> None:
    pass
