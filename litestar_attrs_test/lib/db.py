from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

from lib.constants import dev_user_db_dir, dev_user_db, dev_db_seed

if TYPE_CHECKING:
    ...

import json
from pathlib import Path

db_path = f"{dev_user_db_dir}/{dev_user_db}"

if not Path(dev_user_db_dir).exists():
    print(f"DB directory does not exist: [{dev_user_db_dir}]. Creating.")
    Path(dev_user_db_dir).mkdir(parents=True, exist_ok=True)

db_seed = dev_db_seed


def create_init_db(
    db_path: str = db_path,
    seed_data: dict[int, dict[str, Union[str, int, None]]] = db_seed,
) -> None:
    if not Path(db_path).exists():
        print(f"DB does not exist: {db_path}")
        with open(db_path, "a+") as f_db:
            print(f"Working on DB file: {db_path}")
            json.dump(seed_data, f_db, indent=4)

        f_db.close()


def load_db(db_path: str = db_path) -> dict[str, Any]:
    print(f"Attempting to load DB: {db_path}")

    _continue = True

    while _continue:
        if Path(db_path).exists():
            _continue = False

            print(f"[DEBUG] DB exists: {db_path}")
            with open(db_path, "r") as f_db:
                db_dict = json.loads(f_db.read())
                # print(f"DB dict ({type(db_dict)}): {db_dict}")

            f_db.close()

            return db_dict

        else:
            print(f"[DEBUG] DB does not exist: {db_path}")
            create_init_db(db_path=db_path)

            load_db(db_path=db_path)


def update_db(
    db_path: str = db_path, new_db: dict[Union[int, str], Union[Any, None]] = None
):
    print(f"[DEBUG] Overwriting DB data with: {new_db}")
    print(f"Attempting to load DB: {db_path}")

    _continue = True

    if Path(db_path).exists():
        _continue = False

        print(f"[DEBUG] DB exists: {db_path}")

        with open(db_path, "w+") as f_db:
            json.dump(new_db, f_db, indent=4)

        f_db.close()

        return {"success": f"Database updated successfully."}

    else:
        print(f"[DEBUG] DB does not exist: {db_path}")
        create_init_db(db_path=db_path)

        update_db(db_path=db_path, new_db=new_db)
