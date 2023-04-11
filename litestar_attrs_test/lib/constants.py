"""
Constants that can be imported anywhere in the app. Contains
default values and variables.
"""

from litestar.openapi.spec import Contact, Tag

APP_TITLE = "litestar-testing"
APP_VERSION = "0.0.1"
APP_DESCRIPTION = (
    "Learning environment for Litestar: https://docs.litestar.dev/2/index.html"
)

## Path to documentation site
OPENAPI_DOCS_PATH = "/docs"
## Options: (default) 'redoc', 'swagger', 'elements'
OPENAPI_ROOT_SCHEMA_SITE = "swagger"

STATIC_DIR = "static"
STATIC_PATH = "/static"
FAVICON_PATH = f"{STATIC_PATH}/favicon.ico"


## Initial mock-db (dict), for examples/testing
# dev_user_db_init = {0: {"id": 0, "name": "John Doe"}, 1: {"id": 1, "name": "Jane Doe"}}
dev_user_db_dir = "db"
dev_user_db = "users.json"
dev_db_seed = {
    0: {"id": 0, "name": "John Doe"},
    1: {"id": 1, "name": "Jane Doe"},
    2: {"id": 2, "name": "Test User3"},
}

## Server configuration for consumption by dev_server.py
uvicorn_dev_server_conf = {
    "app": "main:app",
    "host": "0.0.0.0",
    "port": 8120,
    "reload": True,
    "log_level": "debug",
}
