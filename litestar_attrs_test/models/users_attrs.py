from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import attrs


@attrs.define()
class User(object):
    __schema_name__ = "user"
    id: int = attrs.field(default=None)
    name: str = attrs.field(default=None)
