from enum import Enum
import yaml
from pathlib import Path
from typing import Union, Any

from pydantic import BaseSettings, BaseModel, Field, create_model
from pydantic.env_settings import SettingsSourceCallable
from pydantic.utils import deep_update

if __name__ == "__main__":
    ## If this file is run directly, load from config directory
    from config_constants import CONFIG_BASE_DIR, CONF_FILE_DIR
    from utils import load_from_yml, check_yml
    from schemas.app_config import Config
    from schemas.example_config import APIOneConfig
else:
    ## Config was loaded from another file, use full path import
    from lib.config.config_constants import CONFIG_BASE_DIR, CONF_FILE_DIR
    from lib.config.utils import load_from_yml, check_yml
    from lib.config.schemas.app_config import Config
    from lib.config.schemas.example_config import APIOneConfig


if __name__ == "__main__":
    _global = load_from_yml(yml_file=f"{CONF_FILE_DIR}/global.yml")
    _test_deep = load_from_yml(yml_file=f"{CONF_FILE_DIR}/test_deep.yml")

    print(f"[DEBUG] Global config dict: {_global}")
    print(f"[DEBUG] Test deep_load config dict: {_test_deep}")

    test_deep = APIOneConfig(**_test_deep)
    print(f"[DEBUG] test_deep object: {test_deep}")
    print(f"[DEBUG] test_deep.date_format: {test_deep.date_time_format}")

    # print(f"Conf check pass: {check_yml(yml_file=f'{CONF_FILE_DIR}/test_deep.yml')}")

    ## Example will intentionally fail
    #  Uncomment to see exception/error response
    # print(f"Conf check fail: {check_yml(yml_file='nonexist.yml')}")
