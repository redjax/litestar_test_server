"""
Schemas & base configuration for docs page.

The OPENAPI_DOCS_PATH constant defines the route to the docs
site, default "/docs".
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.controller import OpenAPIController
from litestar.openapi.spec import Contact, Tag

from typing import List, Dict, Any, Optional, Union

from lib.constants import (
    OPENAPI_DOCS_PATH,
    OPENAPI_ROOT_SCHEMA_SITE,
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
)

import attrs

if TYPE_CHECKING:
    ...


## Create a custom docs controller to use a different route to docs
class DocsController(OpenAPIController):
    ## Set path to docs site, defaults to OPENAPI_DOCS_PATH constant
    path: str = OPENAPI_DOCS_PATH


## Initialize custom OpenAPIConfig class
class DocsConfig(OpenAPIConfig):
    title: str = APP_TITLE
    description: str = APP_DESCRIPTION
    version: str = APP_VERSION
    tags: List[Tag] = [
        Tag(
            name="example",
            description="Example endpoints to demontrate functionality",
        )
    ]
    use_handler_docstrings: bool = True
    root_schema_site: str = OPENAPI_ROOT_SCHEMA_SITE
    openapi_controller: DocsController = DocsController

    @property
    def conf(self) -> OpenAPIConfig:
        _config = OpenAPIConfig(**self.__dict__)

        return _config


def get_openapi_config(conf: Dict[str, Any] = None) -> DocsConfig:
    """
    Return instance of custom DocsConfig class.

    Defines settings for documentation site.
    """

    try:
        ## Create DocsConfig object from dict passed as conf
        _openapi_config = DocsConfig(**conf)

    except Exception as exc:
        raise Exception(
            f"Unhandled exception creating OpenAPIConfig class. Message:\n{exc}"
        )

    return _openapi_config
