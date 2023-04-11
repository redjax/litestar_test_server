from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import attrs

from litestar import MediaType
from litestar.controller import Controller
from litestar.handlers import get, post, patch, delete
from litestar.partial import Partial

from lib.constants import dev_user_db_init

from models.users import User


class UserController(Controller):
    path = "/user"

    @post()
    async def create_user(self, data: User) -> User:
        ...

    @get("/{user_id:int}")
    def retrieve_user(self, user_id: int) -> dict:
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

    @patch(path="/{user_id:int}")
    async def update_user(self, user_id: int, data: Partial[User]) -> User:
        ...

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int) -> None:
        ...
