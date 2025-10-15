# file: app/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=120)
    completed: bool | None = None

class Todo(TodoBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
