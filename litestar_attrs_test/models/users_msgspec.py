from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import msgspec


class User(msgspec.Struct):
    id: int | None = None
    name: str | None = None
