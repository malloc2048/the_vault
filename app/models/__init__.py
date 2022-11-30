from sqlalchemy import inspect

from .os import OS
from .dvd import DVD
from .cpu import Processor
from .mb import Motherboard
from .gpu import GraphicsCard


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
