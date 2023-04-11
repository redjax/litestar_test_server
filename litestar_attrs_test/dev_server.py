"""
Run a test/dev server with Uvicorn. Useful for running local, non-Dockerized
instance of app.
"""

## Import __future__.annotations, which quotes all anotations "behind the scenes"
from __future__ import annotations

import stackprinter

stackprinter.set_excepthook(style="darkbg2")

## Use TYPE_CHECKING to import modules that would create a circular reference
from typing import TYPE_CHECKING

## TYPE_CHECKING is False in the parser, so this will not run, but the parser will understand bar.Bar
if TYPE_CHECKING:
    ## Put imports here that would cause runtime exceptions for circular imports.
    ...

import uvicorn

import attrs
from typing import Dict, List, Any, Optional, Union

from lib.constants import uvicorn_dev_server_conf


## Class for custom Uvicorn server.
#    Will be extended to include custom logging conf
@attrs.define()
class UvicornCustomServer(object):
    ## Define which app to run. Default to main.py > app()
    app: str = attrs.field(default="main:app")
    host: str = attrs.field(default="0.0.0.0")
    ## Default container (or host, if not runnin in Docker) port to run on
    port: int = attrs.field(default=8000)
    ## Reload server on code change
    reload: bool = attrs.field(default=False)
    ## Logging level for Uvicorn
    log_level: str = attrs.field(default="info")

    def run_server(self):
        """
        Class function, runs a Uvicorn server with self config.
        """

        uvicorn.run(
            app=self.app,
            host=self.host,
            port=self.port,
            reload=self.reload,
            log_level=self.log_level,
            # log_config=self.log_config,
        )


## Dev server configuration defined in lib.constants
dev_conf = uvicorn_dev_server_conf


def main(_server: UvicornCustomServer = UvicornCustomServer()):
    """
    Run custom Uvicorn server.
    """

    _server.run_server()


if __name__ == "__main__":
    dev_server = UvicornCustomServer(**dev_conf)

    main(dev_server)
