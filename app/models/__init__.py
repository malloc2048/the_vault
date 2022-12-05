import json

from .os import OS
from .game import Game
from .movie import Movie
from .cpu import Processor
from .mb import Motherboard
from .gpu import GraphicsCard

import hashlib
from app.utils import object_as_dict, obj_from_dict


categories = {
    'os': OS,
    'mb': Motherboard,
    'cpu': Processor,
    'gpu': GraphicsCard,
    'movie': Movie,
    'game': Game
}


def category_details(details: bool = True) -> list:
    if details:
        cat_details = list()
        for category in categories:
            cat_details.append({
                'name': category,
                'description': categories.get(category)().display_name,
                'group': categories.get(category)().group
            })
        return cat_details
    else:
        return list(categories.keys())


def get_category_display_name(category: str) -> str:
    try:
        return categories.get(category).display_name
    except KeyError:
        return ''


def get_category_data(category: str) -> (list, list):
    try:
        db_data = categories.get(category).query.all()
        attributes = list(object_as_dict(categories.get(category)).keys())
    except KeyError:
        return [], []

    data = list()
    for x in db_data:
        data.append(object_as_dict(x))
    return attributes, data


def get_category_fields(category: str) -> list:
    try:
        return list(object_as_dict(categories.get(category)).keys())
    except KeyError:
        return []


def get_required_category_fields(category: str) -> list:
    try:
        return categories.get(category).field_names()
    except KeyError:
        return []


def add_item(data: dict, category: str, db):
    data_str = json.dumps(data)
    data_hash = hashlib.sha256(data_str.encode('utf-8')).hexdigest()

    # see if this hash is already in the DB, and skip the add if it is
    if category == 'movie':
        hash_entry = categories.get(category).query.filter_by(hash=data_hash).all()
    else:
        hash_entry = None

    # so this hash does not exist go forth with the add
    if not hash_entry:
        try:
            item = categories.get(category)()
            item.hash = data_hash
        except KeyError:
            item = None

        if item and obj_from_dict(item, data) and item.validate(data=data):
            db.session.add(item)
            db.session.commit()
    else:
        # the hash exists. get that row and return the data for it
        item = categories.get(category).query.filter_by(
            hash=data_hash
        ).first()

    return item


def update_item(data: dict, category: str, db):
    # should validate the data before update
    try:
        item = categories.get(category).query.get_or_404(data.get('id'))
    except KeyError:
        item = None

    if item:
        item.from_dict(data)
        db.session.add(item)
        db.session.commit()


def delete_item(data: dict, category: str, db):
    try:
        result = categories.get(category).query.filter_by(id=data.get('id')).all()
    except KeyError:
        result = None

    if result:
        item = result[0]
        db.session.delete(item)
        db.session.commit()
    return result[0]
