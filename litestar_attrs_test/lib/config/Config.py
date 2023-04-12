from enum import Enum
import yaml
from pathlib import Path
from typing import Union, Any

from pydantic import BaseSettings, BaseModel, Field, create_model, SecretStr
from pydantic.env_settings import SettingsSourceCallable
from pydantic.utils import deep_update

## Handle imports of config modules for when script is run directly vs imported
if __name__ == "__main__":
    ## If this file is run directly, load from config directory
    from config_constants import CONF_FILE_DIR, CONFIG_BASE_DIR
    from utils import load_from_yml, check_yml
    from schemas.app_config import Config
    from schemas.example_config import APIOneConfig
    from schemas.openapi_config import OpenapiCustomConfig
else:
    ## Config was loaded from another file, use full path import
    from lib.config.config_constants import CONF_FILE_DIR, CONFIG_BASE_DIR
    from lib.config.utils import load_from_yml, check_yml
    from lib.config.schemas.app_config import Config
    from lib.config.schemas.example_config import APIOneConfig
    from lib.config.schemas.openapi_config import OpenapiCustomConfig

## Create settings dicts to parse into config class objects
check_global_yml = check_yml(f"{CONF_FILE_DIR}/global.yml")
print(f"[DEBUG] Check global config: {check_global_yml}")

if not check_global_yml["success"]:
    raise Exception(f"Unahndled exception loading {f'{CONF_FILE_DIR}/global.yml'}")
_global_dict = load_from_yml(yml_file=f"{CONF_FILE_DIR}/global.yml")
# print(f"[DEBUG] Global dict: {_global_dict}")

check_openapi_yml = check_yml(f"{CONF_FILE_DIR}/openapi.yml")
print(f"[DEBUG] Check OpenAPI config: {check_openapi_yml}")

_openapi_dict = load_from_yml(yml_file=f"{CONF_FILE_DIR}/openapi.yml")
print(f"[DEBUG] OpenAPI dict: {_openapi_dict}")

## Parse dicts into settings objects
app_settings = Config.parse_obj(_global_dict)
# print(f"[DEBUG] Test print secret: {app_settings.secret_test.get_secret_value()}")
openapi_settings = OpenapiCustomConfig.parse_obj(_openapi_dict)


if __name__ == "__main__":
    _test_deep = load_from_yml(yml_file=f"{CONF_FILE_DIR}/test_deep.yml")

    print(f"[DEBUG] Test deep_load config dict: {_test_deep}")

    test_deep = APIOneConfig(**_test_deep)
    print(f"[DEBUG] test_deep object: {test_deep}")
    print(f"[DEBUG] test_deep.date_format: {test_deep.date_time_format}")

    # print(f"Conf check pass: {check_yml(yml_file=f'{CONF_FILE_DIR}/test_deep.yml')}")

    ## Example will intentionally fail
    #  Uncomment to see exception/error response
    # print(f"Conf check fail: {check_yml(yml_file='nonexist.yml')}")
