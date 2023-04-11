from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import attrs

from litestar import MediaType
from litestar.controller import Controller
from litestar.handlers import get, post

from lib.constants import dev_user_db_init

from models.users import User


class UserController(Controller):
    path = "/user"

    @get("/{user_id:int}")
    def get_user(self, user_id: int) -> dict:
        """
        Lookup user by ID. Return a User() object
        """

        _user = dev_user_db_init[user_id]
        print(f"Get User ({type(_user)}): {_user}")

        try:
            user = User(**_user)

        except Exception as exc:
            raise Exception(f"Error creating User object:\n{exc}")

        return user
