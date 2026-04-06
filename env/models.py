from pydantic import BaseModel
from typing import List, Dict, Any


class Observation(BaseModel):
    dataset_preview: List[Dict[str, Any]]
    issues_detected: List[str]
    steps_remaining: int
    quality_score: float


class Action(BaseModel):
    action_type: str
    column: str = None


class Reward(BaseModel):
    value: float
    reason: str


class State(BaseModel):
    dataset: List[Dict[str, Any]]
    issues: List[str]
    steps_left: int
    quality: float