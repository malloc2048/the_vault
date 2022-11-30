from app import db, models


def categories(details: bool = True) -> list:
    if details:
        return [
            {'name': 'mb', 'description': 'Motherboard'},
            {'name': 'gpu', 'description': 'Graphics Card'},
            {'name': 'cpu', 'description': 'Processor'},
            {'name': 'os', 'description': 'Operating Systems'},
            {'name': 'dvd', 'description': 'DVDs'}
        ]
    else:
        return [
            'mb', 'cpu', 'gpu', 'os', 'dvd'
        ]


def get_category_display_name(category: str) -> str:
    if category == 'mb':
        return models.Motherboard.display_name
    elif category == 'cpu':
        return models.Processor.display_name
    elif category == 'gpu':
        return models.GraphicsCard.display_name
    elif category == 'os':
        return models.OS.display_name
    elif category == 'dvd':
        return models.DVD.display_name
    else:
        return ''


def get_category_data(category: str) -> (list, list):
    if category == 'mb':
        db_data = models.Motherboard.query.all()
        attributes = models.Motherboard.display_names()

    elif category == 'cpu':
        db_data = models.Processor.query.all()
        attributes = models.Processor.display_names()

    elif category == 'gpu':
        db_data = models.GraphicsCard.query.all()
        attributes = models.GraphicsCard.display_names()

    elif category == 'os':
        db_data = models.OS.query.all()
        attributes = models.OS.display_names()

    elif category == 'dvd':
        db_data = models.DVD.query.all()
        attributes = models.DVD.display_names()

    else:
        return [], []

    data = list()
    for x in db_data:
        data.append(x.to_dict())
    return attributes, data


def get_category_fields(category: str) -> list:
    if category == 'mb':
        attributes = models.Motherboard.field_names()

    elif category == 'cpu':
        attributes = models.Processor.field_names()

    elif category == 'gpu':
        attributes = models.GraphicsCard.field_names()

    elif category == 'os':
        attributes = models.OS.field_names()

    elif category == 'dvd':
        attributes = models.DVD.field_names()

    else:
        return []
    return attributes


def get_required_category_fields(category: str) -> list:
    if category == 'mb':
        attributes = models.Motherboard.field_names()

    elif category == 'cpu':
        attributes = models.Processor.field_names()

    elif category == 'gpu':
        attributes = models.GraphicsCard.field_names()

    elif category == 'os':
        attributes = models.OS.required_field_names()

    elif category == 'dvd':
        attributes = models.DVD.required_field_names()

    else:
        return []
    return attributes


def add_item(data: dict, category: str):
    item = None
    if category == 'mb':
        item = models.Motherboard()
    elif category == 'cpu':
        item = models.Processor()
    elif category == 'gpu':
        item = models.GraphicsCard()
    elif category == 'os':
        item = models.OS()
    elif category == 'dvd':
        item = models.DVD()

    if item.from_dict(data):
        db.session.add(item)
        db.session.commit()


def update_item(data: dict, category: str):
    # should validate the data before update
    item = None
    if category == 'mb':
        item = models.Motherboard.query.get_or_404(data.get('id'))

    elif category == 'cpu':
        item = models.Processor.query.get_or_404(data.get('id'))

    elif category == 'gpu':
        item = models.GraphicsCard.query.get_or_404(data.get('id'))

    elif category == 'os':
        item = models.OS.query.get_or_404(data.get('id'))

    elif category == 'dvd':
        item = models.DVD.query.get_or_404(data.get('id'))

    if item:
        item.from_dict(data)
        db.session.add(item)
        db.session.commit()


def delete_item(data: dict, category: str):
    if category == 'mb':
        result = models.Motherboard.query.filter_by(id=data.get('id')).all()

    elif category == 'cpu':
        result = models.Processor.query.filter_by(id=data.get('id')).all()

    elif category == 'gpu':
        result = models.GraphicsCard.query.filter_by(id=data.get('id')).all()

    elif category == 'os':
        result = models.OS.query.filter_by(id=data.get('id')).all()

    elif category == 'dvd':
        result = models.DVD.query.filter_by(id=data.get('id')).all()

    else:
        result = None

    if result:
        item = result[0]
        db.session.delete(item)
        db.session.commit()
