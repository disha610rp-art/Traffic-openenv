from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    north_queue: int
    south_queue: int
    east_queue: int
    west_queue: int
    signal: str
    emergency: Optional[str]
    time_step: int

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    reward: float