from sqlalchemy import inspect


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def obj_from_dict(obj, data: dict) -> bool:
    for key in data:
        if key != 'id':
            if data[key]:
                setattr(obj, key, data[key])

    return True
