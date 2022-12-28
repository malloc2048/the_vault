import importlib


categories_module_map = dict()


def load_data_files():
    import os
    import json
    data_file_directory = f'{os.path.abspath(os.path.dirname(__file__))}/data_files'

    data_files = os.listdir(data_file_directory)
    for data_file_name in data_files:
        print(f'[INFO] loading data file {data_file_name}')
        with open(f'{data_file_directory}/{data_file_name}', 'r') as data_file:
            for line in data_file:
                data = json.loads(line)

                # keep track of the loaded model types
                if data.get('model_type'):
                    try:
                        model_module = importlib.import_module(f"app.models.{data.get('model_type')}").model
                        categories_module_map.setdefault(data.get('model_type'), model_module)
                        model_module.add(data.get('data'))

                    except ModuleNotFoundError:
                        # TODO: add a log/error message that data is not loaded for a specific line,
                        #  since there is a typo in the model_type
                        pass


def category_details(details: bool = True) -> list:
    if details:
        cat_details = list()

        for m in categories_module_map.keys():
            cat_details.append({
                'name': m,
                'description': categories_module_map[m].display_name
            })

        return cat_details

    else:
        return list(categories_module_map.keys())


def get_category_display_name(category: str) -> str:
    try:
        return categories_module_map.get(category).display_name
    except KeyError:
        return ''


def get_category_data(category: str) -> (list, list):
    model = categories_module_map.get(category)
    if model:
        data = list()
        display_fields = model.display_fields
        data = model.query()
        return display_fields, data
    return [], []


def get_required_category_fields(category: str) -> list:
    try:
        return categories_module_map.get(category).field_names()
    except KeyError:
        return []


# def add_item(data: dict, category: str, db):
#     data_str = json.dumps(data)
#     data_hash = hashlib.sha256(data_str.encode('utf-8')).hexdigest()
#
#     # see if this hash is already in the DB, and skip the add if it is
#     hash_entry = categories_module_map.get(category).query.filter_by(hash=data_hash).first()
#
#     # so this hash does not exist go forth with the add
#     if not hash_entry:
#         try:
#             item = categories_module_map.get(category)()
#             item.hash = data_hash
#         except KeyError:
#             item = None
#
#         if item and obj_from_dict(item, data) and item.validate(data=data):
#             db.session.add(item)
#             db.session.commit()
#     else:
#         # the hash exists. get that row and return the data for it
#         print(f'[INFO] hash already exists {data_hash}')
#         item = hash_entry
#
#     return item
#
#
# def update_item(data: dict, category: str, db):
#     # should validate the data before update
#     try:
#         item = categories_module_map.get(category).query.get_or_404(data.get('id'))
#     except KeyError:
#         item = None
#
#     if item:
#         item.from_dict(data)
#         db.session.add(item)
#         db.session.commit()
#
#
# def delete_item(data: dict, category: str, db):
#     try:
#         result = categories_module_map.get(category).query.filter_by(id=data.get('id')).all()
#     except KeyError:
#         result = None
#
#     if result:
#         item = result[0]
#         db.session.delete(item)
#         db.session.commit()
#         return item
#     return None

