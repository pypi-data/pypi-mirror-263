# Author: Yiannis Charalambous

import pytest
import os

from pyautoconfig import EnvConfigField, EnvConfigLoader


def test_create_missing_fields() -> None:
    loader: EnvConfigLoader = EnvConfigLoader(
        fields=[
            EnvConfigField("field1", "string"),
            EnvConfigField("field2", 0),
            EnvConfigField("field3", 2.5, is_optional=True),
        ],
        create_missing_fields=True,
        read_sys_env=False,
    )

    assert loader.get_value("field1") == "string"
    assert loader.get_value("field2") == 0
    assert loader.get_value("field3") == 2.5
    assert loader.get_value("aaaaa") == None


def test_load_sys_env() -> None:
    os.environ["ESBMC_TEST_VAR1"] = "1.1"
    os.environ["ESBMC_TEST_VAR2"] = "hello"

    loader: EnvConfigLoader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_VAR1", 1.0),
            EnvConfigField("ESBMC_TEST_VAR2", "AAA"),
            EnvConfigField("ESBMC_TEST_VAR3", 11, is_optional=True),
            EnvConfigField("ESBMC_TEST_VAR4", "BBBBB"),  # This will be None
        ],
        create_missing_fields=False,
    )
    loader.refresh_data(False)

    assert loader.get_value("ESBMC_TEST_VAR1") == 1.1
    assert loader.get_value("ESBMC_TEST_VAR2") == "hello"
    assert loader.get_value("ESBMC_TEST_VAR3") == 11
    assert loader.get_value("ESBMC_TEST_VAR4") == None


def test_detect_missing() -> None:
    with pytest.raises(Exception):
        EnvConfigLoader(
            fields=[
                EnvConfigField("field1", "string"),
                EnvConfigField("field2", 0),
            ],
            create_missing_fields=False,
            fail_on_missing_field=True,
        )

    loader: EnvConfigLoader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_VAR3", 11, is_optional=True),
        ],
        create_missing_fields=False,
    )

    assert loader.get_value("ESBMC_TEST_VAR3") == 11


def test_types() -> None:
    # EnvTypes are: bool | float | int | str
    os.environ["ESBMC_TEST_FALSE"] = "False"
    os.environ["ESBMC_TEST_TRUE"] = "TRUE"
    os.environ["ESBMC_TEST_FLOAT"] = "11.0001"
    os.environ["ESBMC_TEST_INT"] = "123"
    os.environ["ESBMC_TEST_STR"] = "Hello world"

    loader: EnvConfigLoader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_FALSE", False),
            EnvConfigField("ESBMC_TEST_TRUE", True),
            EnvConfigField("ESBMC_TEST_FLOAT", 89.1222),
            EnvConfigField("ESBMC_TEST_INT", 12),
            EnvConfigField("ESBMC_TEST_STR", ""),
        ],
    )
    assert loader.get_value("ESBMC_TEST_FALSE") == False
    assert loader.get_value("ESBMC_TEST_TRUE") == True
    assert loader.get_value("ESBMC_TEST_FLOAT") == 11.0001
    assert loader.get_value("ESBMC_TEST_INT") == 123
    assert loader.get_value("ESBMC_TEST_STR") == "Hello world"


def test_load_single_file() -> None:
    loader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_1", ""),
            EnvConfigField("ESBMC_TEST_2", ""),
            EnvConfigField("ESBMC_TEST_3", 0),
        ],
        read_sys_env=False,
        create_missing_fields=False,
    )

    loader.load_env_file("./samples/.env")

    assert loader.get_value("ESBMC_TEST_1") == "hello world"
    assert loader.get_value("ESBMC_TEST_2") == "hello 2"
    assert loader.get_value("ESBMC_TEST_3") == 12345


def test_load_stacked() -> None:
    loader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_VAR1", 1),
            EnvConfigField("ESBMC_TEST_VAR2", False),
            EnvConfigField("ESBMC_TEST_VAR3", "Hello"),
        ],
        create_missing_fields=False,
        read_sys_env=False,
    )

    loader.load_env_file("samples/dir1/dir2/stacked-test.env")

    assert loader.get_value("ESBMC_TEST_VAR1") == 0
    assert loader.get_value("ESBMC_TEST_VAR2") == False
    assert loader.get_value("ESBMC_TEST_VAR3") == "This should change"


def test_dont_read_sys_env() -> None:
    # We dont want to read the env vars in this test.

    os.environ["ESBMC_TEST_VAR1"] = "11.2"
    os.environ["ESBMC_TEST_VAR2"] = "False"
    os.environ["ESBMC_TEST_VAR3"] = "AAA"

    loader = EnvConfigLoader(
        fields=[
            EnvConfigField("ESBMC_TEST_VAR1", 0.0, is_optional=True),
            EnvConfigField("ESBMC_TEST_VAR2", True, is_optional=True),
            EnvConfigField("ESBMC_TEST_VAR3", "Hello", is_optional=True),
        ],
        create_missing_fields=True,
        read_sys_env=False,
    )

    assert loader.get_value("ESBMC_TEST_VAR1") == 0.0
    assert loader.get_value("ESBMC_TEST_VAR2") == True
    assert loader.get_value("ESBMC_TEST_VAR3") == "Hello"
