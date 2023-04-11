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

from lib.db import load_db, update_db


class UserController(Controller):
    path = "/user"

    @post()
    async def create_user(self, data: User) -> dict[str, Any]:
        print(f"Creating user from: {data}")

        try:
            _db = load_db()
            # print(f"Loaded DB: Type: {type(_db)}, contents:\n{_db}")

        except Exception as exc:
            raise Exception(f"Error loading database. Exception details:\n{exc}")

        users_keys = _db.keys()
        users_values = _db.values()

        if str(data.id) in users_keys:
            print(f"[DEBUG] Found ID: '{data.id}' in DB keys. Skipping user creation")

            return {
                "skipped": f"User with ID '{data.id}' already exists. Skipping creation."
            }

        else:
            # print(f"[DEBUG] User not found with ID '{data.id}'. Continuing.")
            new_user = {data.id: {"id": data.id, "name": data.name}}
            # print(f"[DEBUG] New user: {new_user}")

            _db.update(new_user)
            # print(f"Updated DB: {_db}")

            _new_user_res = update_db(new_db=_db)

            # print(f"New user creation results: {_new_user_res}")

            return _new_user_res

    @get("/{user_id:int}")
    def retrieve_user(self, user_id: int) -> dict:
        """
        Lookup user by ID. Return a User() object
        """

        try:
            # print(f"[DEBUG] Retrieving user with ID: {user_id}")
            _db = load_db()
            # print(f"Loaded DB: Type: {type(_db)}, contents:\n{_db}")

        except Exception as exc:
            raise Exception(f"Error loading database. Exception details:\n{exc}")

        users_keys = _db.keys()
        users_values = _db.values()

        if str(user_id) in users_keys:
            print(f"[DEBUG] Found ID: '{user_id}' in DB keys.")

            try:
                for _user in users_values:
                    print(f"[DEBUG] User: {_user}")

                    if _user["id"] == user_id:
                        # print(f"[DEBUG] Matched user_id '{user_id}' to DB User: {_user['id']}")

                        user = User.parse_obj(_user)
                        print(f"[DEBUG] Parsed User: {user}")

                        return user

            except Exception as exc:
                raise Exception(
                    f"[ERROR] Error retrieving user with ID [{user_id}] from database. Exception details: {exc}"
                )

        else:
            return {"error": f"User with ID '{user_id}' not found in database."}

    @patch(path="/{user_id:int}")
    async def update_user(self, user_id: int, data: Partial[User]) -> User:
        print(f"Partial update: ID: {user_id} - {data}")

        try:
            # print(f"[DEBUG] Retrieving user with ID: {user_id}")
            _db = load_db()
            # print(f"Loaded DB: Type: {type(_db)}, contents:\n{_db}")

        except Exception as exc:
            raise Exception(f"Error loading database. Exception details:\n{exc}")

        users_keys = _db.keys()
        users_values = _db.values()

        if str(user_id) in users_keys:
            print(f"[DEBUG] [DEBUG] Found ID: '{user_id}' in DB keys.")

            try:
                for _user in users_values:
                    # print(f"[DEBUG] User: {_user}")

                    if _user["id"] == user_id:
                        print(
                            f"[DEBUG] Matched user_id '{user_id}' to DB User: ({type(_user['id'])}) {_user}"
                        )
                        update_user = {user_id: data.dict()}
                        print(f"[DEBUG] New user: {update_user}")

                        user = User.parse_obj(update_user[user_id])
                        print(f"[DEBUG] Parsed User: {user}")

                        _db[str(user_id)] = update_user[user_id]
                        print(f"[DEBUG] Updated DB: {_db}")

                        try:
                            _update_res = update_db(new_db=_db)

                            return _update_res

                        except Exception as exc:
                            return {
                                "error": f"Error performing partial update on User with ID '{user_id}'. Exception details:\n{exc}"
                            }

            except Exception as exc:
                raise Exception(
                    f"[ERROR] Error retrieving user with ID [{user_id}] from database. Exception details: {exc}"
                )

        else:
            return {"error": f"User with ID '{user_id}' not found in database."}

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int) -> None:
        print(f"Deleting user with ID: {user_id}")

        try:
            # print(f"[DEBUG] Retrieving user with ID: {user_id}")
            _db = load_db()
            # print(f"Loaded DB: Type: {type(_db)}, contents:\n{_db}")

        except Exception as exc:
            raise Exception(f"Error loading database. Exception details:\n{exc}")

        users_keys = _db.keys()
        users_values = _db.values()

        if str(user_id) in users_keys:
            print(f"[DEBUG] [DEBUG] Found ID: '{user_id}' in DB keys.")

            try:
                _db.pop(str(user_id))
                print(f"Deleted User with ID '{user_id}'. New database: {_db}")

                _delete_user_res = update_db(new_db=_db)
                print(f"[DEBUG] Delete user results: {_delete_user_res}")

                return _delete_user_res

            except Exception as exc:
                raise Exception(
                    f"Error trying to delete User with ID '{user_id}'. Exception details:\n{exc}"
                )

        else:
            return {"error": f"User with ID '{user_id}' not found in database."}
