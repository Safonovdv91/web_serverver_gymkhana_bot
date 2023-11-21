from typing import Literal

from pydantic import BaseModel


class SportClassSchema(BaseModel):
    sport_class: Literal[
        "A", "B", "C1", "C2", "C3", "D1", "D2", "D3", "D4", "N"
    ]
    description: str | None


class SportClassResponseOne(BaseModel):
    # id: int
    sport_class: str
    description: str


class SportClassResponseMany(BaseModel):
    status: str
    data: list[SportClassSchema]
    details: str | dict | None
