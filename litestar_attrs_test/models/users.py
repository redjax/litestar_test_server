from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import attrs


@attrs.define()
class User(object):
    id: int
    name: str
