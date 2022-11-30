from flask import request
from flask_restx import Resource
from app import api, utils, motherboards


@motherboards.route('/')
class Motherboards(Resource):
    @api.doc(params={
        'make': 'who made the CPU',
        'model': 'the specific CPU',
        'socket': 'how do you plug it in'
    })
    @api.response(200, 'returns a list of all available motherboards')
    def get(self):
        args = request.args

        filter_data = dict()
        if args.get('make'):
            filter_data.setdefault('make', args.get('make'))
        if args.get('model'):
            filter_data.setdefault('model', args.get('model'))
        if args.get('socket'):
            filter_data.setdefault('socket', args.get('socket'))

        all_mb_data = utils.get_category_data('mb')[1]
        if not filter_data:
            return {'mb': all_mb_data}
        else:
            filtered_data = list()
            for mb in all_mb_data:
                shared_items = {k: filter_data[k] for k in filter_data if k in mb and filter_data[k] == mb[k]}
                if len(shared_items) == len(filter_data):
                    filtered_data.append(mb)
            return {'mb': filtered_data}

    @api.doc(params={
        'id': 'if provided the record will be updated',
        'make': 'who made the motherboard',
        'model': 'the specific motherboard',
        'status': 'does it work or not',
        'socket': 'how do you plug it in'
    })
    def post(self):
        fields = utils.get_category_fields('mb')
        args = request.args

        data = dict()
        for field in fields:
            if args.get(field):
                data.setdefault(field, args.get(field))

        if len(fields) == len(data) and 'id' not in args:
            utils.add_item(data, category='mb')
        elif 'id' in args:
            data.setdefault('id', args.get('id'))
            utils.update_item(data, category='mb')

    @api.doc(params={
        'id': 'database id to delete'
    })
    def delete(self):
        id_arg = request.args.get('id')

        if id_arg:
            utils.delete_item({'id': id_arg}, 'mb')


@motherboards.route('/<id>')
class MotherboardsById(Resource):
    @api.response(200, 'return details of a specific mb')
    def get(self, id):
        from app.models import Motherboard, object_as_dict
        results = Motherboard.query.get(id)
        return {'mb': object_as_dict(results)}

