# Author: Yiannis Charalambous


from abc import abstractmethod
import os
from typing import Optional


class BaseConfigLoader(object):
    """Abstract class that contains low level (abstract) methods for loading configs."""

    def __init__(
        self,
        content: Optional[str],
        create_missing_fields: bool = False,
    ) -> None:
        """Initializes the config loader, and if `content` is `None`, then will automatically
        set the value to `_init_defaults()`, and then calls `_read_fields`.

        Args:
            * content - The content of the config to parse. If `None` and `create_missing_fields`
            is True, then will create from the default schema.
            * create_missing_fields - When enabled, then if a field is missing and is not optional,
            will initialize it from defaults. So this means if the config does not match the schema,
            the schema defaults will replace the incompatible values to make it adhere to the schema.
        """

        if content is None:
            if create_missing_fields:
                # Ensure default content.
                content = self._init_defaults()
            else:
                raise ValueError()

        self.raw_content: str = content

        # Read fields.
        self._read_fields(create_missing_fields=create_missing_fields)

    @abstractmethod
    def _init_defaults(self) -> str:
        """Initializes a default state from the schema, and returns a string representation. This method
        is called prior to parsing the content if `create_missing_fields` is True."""
        raise NotImplementedError()

    @abstractmethod
    def _read_fields(self, create_missing_fields: bool = False) -> None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, file_path: str) -> None:
        raise NotImplementedError()
