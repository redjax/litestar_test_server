from pydantic import BaseModel, Field, validator, ValidationError
from typing import Dict, Any, List, Optional

from pathlib import Path

import yaml

supported_filetypes = [".yml"]


def parse_config(file) -> dict:
    """
    Open a config file. Returns a Python dict.

    Currently supports:
        - .yml/yaml

    Example use:
        Load the default config from a file, i.e. config.yml.
        Classes that inherit from the base ConfigBase class
        can use variables/sections in the config.yml file.
    """

    config_name = str(Path(file).name)
    config_filetype = str(Path(file).suffix)

    if config_filetype == ".yml":
        ## Open yaml file for parsing
        with open(file) as f:
            ## Use yaml's safe_load() method
            config = yaml.safe_load(f)

    return config


class ConfigBase(BaseModel):
    """
    Base configuration file. By default, will load configuration from
    a config.yml file, which can be overrided when creating the class.
    I.e. base_config = ConfigBase(file="some-yaml-file.yml")
    """

    file: Optional[str] = "config.yml"

    @property
    def config(self) -> dict:
        """
        Parse config from file
        """

        ## Parse configuration file. Uses the class's 'file' property
        _config = parse_config(self.file)

        return _config

    def get_property(self, key_name: str = None, property_name: str = None):
        if key_name not in self.config.keys():
            return None

        else:
            if property_name not in self.config[key_name].keys():
                return None

            # print(f"Found property: [{property_name}] in key: {key_name}")
            return self.config[key_name][property_name]


class AppConfig(ConfigBase):
    @property
    def name(self) -> str:
        return self.get_property("APP", "APP_NAME")

    @property
    def description(self) -> str:
        return self.get_property("APP", "APP_DESCRIPTION")

    @property
    def version(self) -> int:
        return self.get_property("APP", "APP_VERSION")


class LogConfig(ConfigBase):
    @property
    def level(self):
        return self.get_property("LOG", "LOG_LEVEL")

    @property
    def file(self):
        return self.get_property("LOG", "LOG_FILE")


class DBConfig(ConfigBase):
    @property
    def type(self):
        return self.get_property("DB", "DB_TYPE")

    @property
    def file(self):
        return self.get_property("DB", "DB_FILE")

    @property
    def port(self):
        return self.get_property("DB", "DB_PORT")


## Initialize base config class
base_config = ConfigBase()

## Initialize app settings
app_settings = AppConfig()
## Initialize log settings
log_settings = LogConfig(file="log_config.yml")
## Initialize db settings
db_settings = DBConfig()

## Debug print files
print(f"Log settings: \n\t[Level: {log_settings.level}]\n\t[File: {log_settings.file}]")
print(
    f"DB settings: \n\t[Type: {db_settings.type}]\n\t[File: {db_settings.file}]\n\t[Port: {db_settings.port}]"
)
