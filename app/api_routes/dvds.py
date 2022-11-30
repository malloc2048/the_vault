from flask import request
from flask_restx import Resource
from app import api, utils, dvds


@dvds.route('/')
class Dvds(Resource):
    @api.doc(params={
        'title': 'who made the CPU',
        'director': 'the specific CPU',
        'release_date': 'how fast does it cpu',
    })
    @api.response(200, 'returns a list of all available processors')
    def get(self):
        args = request.args

        filter_data = dict()
        if args.get('title'):
            filter_data.setdefault('title', args.get('title'))
        if args.get('director'):
            filter_data.setdefault('director', args.get('director'))
        if args.get('release_date'):
            filter_data.setdefault('release_date', args.get('release_date'))

        all_data = utils.get_category_data('dvd')[1]
        if not filter_data:
            return {'dvds': all_data}
        else:
            filtered_data = list()
            for item in all_data:
                shared_items = {k: filter_data[k] for k in filter_data if k in item and filter_data[k] == item[k]}
                if len(shared_items) == len(filter_data):
                    filtered_data.append(item)
            return {'dvds': filtered_data}

    @api.doc(params={
        'id': 'if provided the record will be updated',
        'title': 'who made the CPU',
        'director': 'the specific CPU',
        'release_date': 'how fast does it cpu',
    })
    def post(self):
        fields = utils.get_category_fields('dvd')
        args = request.args

        data = dict()
        for field in fields:
            if args.get(field):
                data.setdefault(field, args.get(field))

        if len(fields) == len(data) and 'id' not in args:
            utils.add_item(data, category='dvd')
        elif 'id' in args:
            data.setdefault('id', args.get('id'))
            utils.update_item(data, category='dvd')

    @api.doc(params={
        'id': 'database id to delete'
    })
    def delete(self):
        id_arg = request.args.get('id')

        if id_arg:
            utils.delete_item({'id': id_arg}, 'dvd')


@dvds.route('/<id>')
class ProcessorsByID(Resource):
    @api.response(200, 'return details of a specific DVD')
    def get(self, id):
        from app.models import DVD, object_as_dict
        results = DVD.query.get(id)
        return {'dvds': object_as_dict(results)}
