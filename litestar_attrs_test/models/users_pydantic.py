from pydantic import BaseModel, UUID4


class User(BaseModel):
    id: int
    name: str
