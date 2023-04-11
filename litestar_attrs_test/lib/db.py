from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional, Any

from lib.constants import dev_user_db_dir, dev_user_db

if TYPE_CHECKING:
    ...

import json
from pathlib import Path

db_path = f"{dev_user_db_dir}/{dev_user_db}"

if not Path(dev_user_db_dir).exists():
    print(f"DB directory does not exist: [{dev_user_db_dir}]. Creating.")
    Path(dev_user_db_dir).mkdir(parents=True, exist_ok=True)

db_seed = {0: {"id": 0, "name": "John Doe"}, 1: {"id": 1, "name": "Jane Doe"}}


def create_init_db(
    db_path: str = db_path,
    seed_data: dict[int, dict[str, Union[str, int, None]]] = db_seed,
):
    if not Path(db_path).exists():
        print(f"DB does not exist: {db_path}")
        with open(db_path, "a+") as f_db:
            print(f"Working on DB file: {db_path}")
            _dump = json.load(seed_data)
            f_db.write(_dump)


def load_db(db_path: str = db_path) -> json.Dict:
    print(f"Attempting to load DB: {db_path}")
    if Path(db_path).exists():
        print(f"[DEBUG] DB exists: {db_path}")
        with open(db_path, "r") as f_db:
            db_dict = json.loads(f_db.read())

            print(f"DB dict ({type(db_dict)}): {db_dict}")

    else:
        print(f"[DEBUG] DB does not exist: {db_path}")
        create_init_db(db_path=db_path)
