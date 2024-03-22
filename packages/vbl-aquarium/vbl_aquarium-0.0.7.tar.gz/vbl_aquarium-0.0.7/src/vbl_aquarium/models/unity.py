from pydantic import BaseModel, Field
from typing_extensions import Annotated

# Unity models don't get generated as .cs files since they exist in UnityEngine


class Color(BaseModel):
    r: Annotated[float, Field(ge=0, le=1)]
    g: Annotated[float, Field(ge=0, le=1)]
    b: Annotated[float, Field(ge=0, le=1)]
    a: Annotated[float, Field(default=1, ge=0, le=1)]


class Vector2(BaseModel):
    x: float = 0.0
    y: float = 0.0


class Vector3(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


class Vector4(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0
