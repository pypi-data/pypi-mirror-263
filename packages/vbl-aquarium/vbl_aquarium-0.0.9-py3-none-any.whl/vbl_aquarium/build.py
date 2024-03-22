from enum import Enum
from json import dumps
from os import makedirs
from os.path import abspath, dirname, exists

from vbl_aquarium.generate_cs import pydantic_to_csharp
from vbl_aquarium.models import dock, ephys_link, generic, logging, pinpoint, unity, urchin
from vbl_aquarium.utils.common import get_classes
from vbl_aquarium.utils.vbl_base_model import VBLBaseModel


def remove_ignored_classes(module):
    return [c for c in get_classes(module) if c not in ignored_classes]


ignored_classes = get_classes(unity)
ignored_classes.append(Enum)
ignored_classes.append(VBLBaseModel)
unity_class_names = [x.__name__ for x in get_classes(unity)]

module_list = [generic, urchin, logging, pinpoint, ephys_link, dock]
folder_prefix = ["generic", "urchin", "logging", "pinpoint", "ephys_link", "dock"]

cdir = dirname(abspath(__file__))

for _, (module, cfolder) in enumerate(zip(module_list, folder_prefix)):
    classes = remove_ignored_classes(module)

    for cclass in classes:
        if cclass.__name__ not in unity_class_names:
            path = f"{cdir}/../../models/schemas/{cfolder}"
            if not exists(path):
                makedirs(path)

            with open(f"{path}/{cclass.__name__}.json", "w") as f:
                f.write(dumps(cclass.model_json_schema()))

            path = f"{cdir}/../../models/csharp/{cfolder}"
            if not exists(path):
                makedirs(path)

            with open(f"{path}/{cclass.__name__}.cs", "w") as f:
                f.write(pydantic_to_csharp(cclass, cclass.model_json_schema()))
