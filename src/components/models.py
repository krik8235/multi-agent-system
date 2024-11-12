from typing import Dict
from pydantic import BaseModel, Field, ValidationError
from pydantic.dataclasses import dataclass


class AgentOutput(BaseModel):
    """Output of each clause agent"""

    analysis: str = Field(description="An analysis of the section in laymen terms", max_length=256)
    recommendation: str = Field(
        description="How the current clause deviates from the benchmark documents",
        max_length=256
    )


class FinalOutput(BaseModel):
    data: Dict[str, AgentOutput]