from vbl_aquarium.utils.vbl_base_model import VBLBaseModel

# File IO


class BucketModel(VBLBaseModel):
    token: str
    bucket: str
    password: str


class SaveModel(VBLBaseModel):
    bucket: str
    password: str


class SaveManagerModel(VBLBaseModel):
    bucket: str
    manager: str
    password: str


class LoadModel(VBLBaseModel):
    bucket: str
