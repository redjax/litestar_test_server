from pydantic import BaseModel, UUID4, validator


class User(BaseModel):
    id: int
    name: str

    @validator("id", pre=True, always=True)
    def set_id_int(cls, v, values, **kwargs):
        return int(v, 16) if isinstance(v, str) else v
