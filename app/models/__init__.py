from .os import OS
from .dvd import DVD
from .cpu import Processor
from .mb import Motherboard
from .pc_game import PCGame
from .gpu import GraphicsCard
from .console_game import ConsoleGame
from app.utils import object_as_dict


categories = {
    'mb': Motherboard,
    'pc': PCGame,
    'os': OS,
    'cpu': Processor,
    'gpu': GraphicsCard,
    'dvd': DVD,
    'console': ConsoleGame,
}


def category_details(details: bool = True) -> list:
    if details:
        cat_details = list()
        for category in categories:
            cat_details.append({
                'name': category,
                'description': categories.get(category)().display_name
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
    try:
        item = categories.get(category)()
    except KeyError:
        item = None

    if item.from_dict(data):
        db.session.add(item)
        db.session.commit()
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
