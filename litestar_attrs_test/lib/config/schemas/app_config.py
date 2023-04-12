from pydantic import BaseSettings, Field


class Config(BaseSettings):
    app_title: str = Field(default="UNNAMED_APP", env="APP_TITLE")
    app_description: str = Field(default="DEFAULT_DESCRIPTION", env="APP_DESCRIPTION")
    app_version: str = Field(default="0.1", env="APP_VERSION")
