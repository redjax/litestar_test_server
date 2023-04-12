from typing import Optional
from pydantic import BaseSettings, Field, SecretStr


class Config(BaseSettings):
    app_title: str = Field(default="UNNAMED_APP", env="app_title")
    app_description: str = Field(default="DEFAULT_DESCRIPTION", env="app_description")
    app_version: str = Field(default="0.1", env="app_version")
    secret_test: Optional[SecretStr] = Field(env="secret_test")
