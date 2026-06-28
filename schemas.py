from pydantic import BaseModel
from typing import Optional

# Fields shared by both requests and responses
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# Structure required when creating a task (Request Body)
class TaskCreate(TaskBase):
    pass

# Structure guaranteed when returning a task (Response Body)
class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models smoothly