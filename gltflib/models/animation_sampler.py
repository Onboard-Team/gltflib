from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from .base_model import BaseModel


class Interpolation(Enum):
    LINEAR = 'LINEAR'
    STEP = 'STEP'
    CUBICSPLINE = 'CUBICSPLINE'


@dataclass
@dataclass_json
class AnimationSampler(BaseModel):
    """
    Combines input and output accessors with an interpolation algorithm to define a keyframe graph (but not its target).

    Properties:
    input (integer) The index of an accessor containing keyframe input values, e.g., time. (Required)
    interpolation (string) Interpolation algorithm. (Optional, default: "LINEAR")
    output (integer) The index of an accessor, containing keyframe output values. (Required)
    extensions (object) Dictionary object with extension-specific objects. (Optional)
    extras (any) Application-specific data. (Optional)
    """
    input: int = None
    interpolation: Optional[str] = None
    output: int = None
