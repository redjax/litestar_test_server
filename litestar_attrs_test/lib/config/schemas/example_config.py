from typing import Any
from pydantic import BaseSettings


class APIOneConfig(BaseSettings):
    """
    This is an example, arbitrary class. It loads from conf_files/test_deep.yml

    This .yml file is nested, to demonstrate loading nested data. The class object
    has 1 parameter, "test_api_one," which is a dict object loaded from the .yml file.
    Properties are created from dict values.
    """

    test_api_one: dict[str, Any]

    @property
    def date_format(self) -> str:
        _date_format = self.test_api_one["date_format"]

        return _date_format

    @property
    def date_time_format(self) -> str:
        _date_time_format = self.test_api_one["date_time_format"]

        return _date_time_format
