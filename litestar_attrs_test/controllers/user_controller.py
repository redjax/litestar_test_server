from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

if TYPE_CHECKING:
    ...

import attrs

from litestar import MediaType
from litestar.controller import Controller
from litestar.handlers import get, post, patch, delete
from litestar.partial import Partial

# from lib.constants import dev_user_db_init

# from models.users_attrs import User

# from models.users_msgspec import User
from models.users_pydantic import User

from lib.db import load_db


class UserController(Controller):
    path = "/user"

    @post()
    async def create_user(self, data: User) -> dict[str, Any]:
        print(f"Creating user from: {data}")

        # new_user = {data.id: {"id": data.id, "name": data.name}}
        # dev_user_db_init.update(new_user)
        # print(f"Updated dev_user_db_init dict: {dev_user_db_init}")

        # return {"success": f"Created user {data.name} with ID {data.id}"}

    @get("/{user_id:int}")
    def retrieve_user(self, user_id: int) -> dict:
        """
        Lookup user by ID. Return a User() object
        """

        print(f"Retrieving user with ID: {user_id}")

        _db = load_db()
        print(f"Database: {_db}")

        # _user = dev_user_db_init[user_id]
        # print(f"Get User ({type(_user)}): {_user}")

        # try:
        #     user = User(**_user)

        # except Exception as exc:
        #     raise Exception(f"[Exception] Error retrieving User object:\n{exc}")

        # return user

    @patch(path="/{user_id:int}")
    async def update_user(self, user_id: int, data: Partial[User]) -> User:
        print(f"Partial update: ID: {user_id} - {data}")

        # _update_user = {user_id: {"id": user_id, "name": data.name}}
        # dev_user_db_init.update(_update_user)

        # print(f"Updated dict: {dev_user_db_init}")

        # return {"success": f"Updated user with ID '{user_id}': {data}"}

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int) -> None:
        print(f"Deleting user with ID: {user_id}")
