from __future__ import annotations

from enum import Enum

from pydantic import Field

from vbl_aquarium.models.unity import Color, Vector2, Vector3
from vbl_aquarium.utils.vbl_base_model import VBLBaseModel

# CustomAtlas


class CustomAtlasModel(VBLBaseModel):
    name: str
    dimensions: Vector3
    resolution: Vector3


# CustomMesh


class CustomMeshData(VBLBaseModel):
    id: str = Field(alias="ID")
    vertices: list[Vector3]
    triangles: list[int]
    normals: list[Vector3] = None


class CustomMeshModel(VBLBaseModel):
    id: str = Field(alias="ID")
    position: Vector3
    use_reference: bool
    material: str
    scale: Vector3
    color: Color


# Area


class AreaGroupData(VBLBaseModel):
    acronyms: list[str]
    visible: list[bool]
    side: list[int]


# Camera


class CameraModel(VBLBaseModel):
    class CameraMode(str, Enum):
        orthographic = "orthographic"
        perspective = "perspective"

    id: float
    type: str
    position: Vector3
    rotation: Vector3
    target: Vector3
    zoom: float
    pan: Vector2
    mode: CameraMode
    controllable: bool
    main: bool


# Individual mesh neuron


class MeshModel(VBLBaseModel):
    id: str = Field(alias="ID")
    shape: str
    position: Vector3
    color: Color
    scale: Vector3
    material: str
    interactive: bool


# Particle group


class ParticleGroupModel(VBLBaseModel):
    id: str = Field(alias="ID")
    scale: Vector3
    shape: str
    material: str

    xs: list[float]
    ys: list[float]
    zs: list[float]

    colors: list[Color]
