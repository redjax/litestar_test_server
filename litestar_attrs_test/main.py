from __future__ import annotations
import stackprinter

stackprinter.set_excepthook(style="darkbg2")


from typing import TYPE_CHECKING, Dict, Union, Optional, Any

## Import app constants/defaults
from lib.constants import (
    APP_TITLE,
    APP_DESCRIPTION,
    APP_VERSION,
    OPENAPI_ROOT_SCHEMA_SITE,
    OPENAPI_DOCS_PATH,
    dev_user_db_init,
)

## Import custom openapi_docs classes/functions
from schemas.openapi_docs import (
    DocsConfig,
    DocsController,
    get_openapi_config,
)


if TYPE_CHECKING:
    ...


from litestar import Litestar, get, MediaType

from controllers.root_controller import RootController


## Create docs config dict
openapi_config_dict = {
    "title": APP_TITLE,
    "description": APP_DESCRIPTION,
    "version": APP_VERSION,
    "root_schema_site": OPENAPI_ROOT_SCHEMA_SITE,
    # "tags": [Tag(name=..., description=...)],
    "openapi_controller": DocsController,
}

## Create OpenAPIConfig object
openapi_config = get_openapi_config(conf=openapi_config_dict)
print(f"[DEBUG] Docs config: {openapi_config}")
print(f"[DEBUG] Docs Controller: {openapi_config.openapi_controller.__dict__}")

## Create Litestar app
app = Litestar(
    ## Add route handlers/controllers to app
    route_handlers=[RootController],
    ## Add custom OpenAPI config for docs site
    openapi_config=openapi_config,
)

if __name__ == "__main__":
    ...
