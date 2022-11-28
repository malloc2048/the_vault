from app import db, models


def categories(details: bool = True) -> list:
    if details:
        return [
            {'name': 'mb', 'description': 'Motherboard'},
            {'name': 'gpu', 'description': 'Graphics Card'},
            {'name': 'cpu', 'description': 'Processor'},
            {'name': 'os', 'description': 'Operating Systems'}
        ]
    else:
        return [
            'mb', 'cpu', 'gpu', 'os'
        ]


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

    else:
        return [], []

    data = list()
    for x in db_data:
        data.append(x.to_dict())
    return attributes, data


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

    if item.from_dict(data):
        db.session.add(item)
        db.session.commit()


def update_item(data: dict, category: str):
    # should validate the data before update
    item = None
    if category == 'mb':
        item = models.Motherboard.query.get_or_404(data.get('ID'))

    elif category == 'cpu':
        item = models.Processor.query.get_or_404(data.get('ID'))

    elif category == 'gpu':
        item = models.GraphicsCard.query.get_or_404(data.get('ID'))

    elif category == 'os':
        item = models.OS.query.get_or_404(data.get('ID'))

    if item:
        item.from_dict(data)
        db.session.add(item)
        db.session.commit()


def delete_item(data: dict, category: str):
    if category == 'mb':
        result = models.Motherboard.query.filter_by(id=data.get('ID')).all()

    elif category == 'cpu':
        result = models.Processor.query.filter_by(id=data.get('ID')).all()

    elif category == 'gpu':
        result = models.GraphicsCard.query.filter_by(id=data.get('ID')).all()
    else:
        result = None

    if result:
        item = result[0]
        db.session.delete(item)
        db.session.commit()
