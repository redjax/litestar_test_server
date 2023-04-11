"""
Controller for root / path. Handles routes for hello_world
and healthcheck.

Import this controller in a Litestar.app with route_handlers=[root_controller]
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

from litestar import MediaType
from litestar.controller import Controller
from litestar.handlers import get, post


class RootController(Controller):
    """
    Controller for root / path.

    Has endpoints for / (hello_world) and
    /healtcheck (health_check)
    """

    path = "/"

    ## Create root route
    @get(path="/", media_type=MediaType.TEXT)
    async def hello_world(self) -> Dict[str, str]:
        return {"hello": "world"}

    ## Create health check route
    @get(path="/healthcheck", media_type=MediaType.TEXT)
    async def health_check(self) -> str:
        return "healthy"
