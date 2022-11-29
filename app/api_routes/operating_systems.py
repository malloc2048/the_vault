from flask import request
from flask_restx import Resource
from app import api, utils, operating_systems


@operating_systems.route('/')
class Motherboards(Resource):
    @api.doc(params={
        'publisher': 'who made the OS',
        'name': 'the specific OS',
        'version': 'The version'
    })
    @api.response(200, 'returns a list of all available OSes')
    def get(self):
        args = request.args

        filter_data = dict()
        if args.get('publisher'):
            filter_data.setdefault('publisher', args.get('publisher'))
        if args.get('name'):
            filter_data.setdefault('name', args.get('name'))
        if args.get('version'):
            filter_data.setdefault('version', args.get('version'))

        all_os_data = utils.get_category_data('os')[1]
        if not filter_data:
            return {'os': all_os_data}
        else:
            # TODO: there is an opportunity to pull this out to a function same for all so far
            filtered_data = list()
            for os in all_os_data:
                shared_items = {k: filter_data[k] for k in filter_data if k in os and filter_data[k] == os[k]}
                if len(shared_items) == len(filter_data):
                    filtered_data.append(os)
            return {'os': filtered_data}

    @api.doc(params={
        'id': 'if provided the record will be updated',
        'publisher': 'who made the motherboard',
        'name': 'the specific motherboard',
        'version': 'does it work or not',
    })
    def post(self):
        fields = utils.get_required_category_fields('os')
        args = request.args

        data = dict()
        for field in fields:
            if args.get(field):
                data.setdefault(field, args.get(field))
        print(len(fields) == len(data))

        if len(fields) == len(data) and 'id' not in args:
            utils.add_item(data, category='os')
        elif 'id' in args:
            data.setdefault('id', args.get('id'))
            utils.update_item(data, category='os')

    @api.doc(params={
        'id': 'database id to delete'
    })
    def delete(self):
        id_arg = request.args.get('id')

        if id_arg:
            utils.delete_item({'id': id_arg}, 'os')


@operating_systems.route('/<id>')
class MotherboardsById(Resource):
    @api.response(200, 'return details of a specific OS record')
    def get(self, id):
        from app.models import Processor, object_as_dict
        results = Processor.query.get(id)
        return {'os': object_as_dict(results)}
