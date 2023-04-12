from typing import Optional
from pydantic import BaseSettings, Field, SecretStr


class OpenapiCustomConfig(BaseSettings):
    root_schema_site: str = Field(env="root_schema_site")
