from flask import request
from flask_restx import Resource
from app import api, utils, processors


@processors.route('/')
class Processors(Resource):
    @api.doc(params={
        'make': 'who made the CPU',
        'model': 'the specific CPU',
        'frequency': 'how fast does it cpu',
        'socket': 'how do you plug it in'
    })
    @api.response(200, 'returns a list of all available processors')
    def get(self):
        args = request.args

        filter_data = dict()
        if args.get('make'):
            filter_data.setdefault('make', args.get('make'))
        if args.get('model'):
            filter_data.setdefault('model', args.get('model'))
        if args.get('socket'):
            filter_data.setdefault('socket', args.get('socket'))
        if args.get('frequency'):
            filter_data.setdefault('frequency', int(args.get('frequency')))

        all_cpu_data = utils.get_category_data('cpu')[1]
        if not filter_data:
            return {'cpus': all_cpu_data}
        else:
            filtered_data = list()
            for cpu in all_cpu_data:
                shared_items = {k: filter_data[k] for k in filter_data if k in cpu and filter_data[k] == cpu[k]}
                if len(shared_items) == len(filter_data):
                    filtered_data.append(cpu)
            return {'cpus': filtered_data}

    @api.doc(params={
        'id': 'if provided the record will be updated',
        'make': 'who made the CPU',
        'model': 'the specific CPU',
        'frequency': 'how fast does it cpu',
        'socket': 'how do you plug it in'
    })
    def post(self):
        fields = utils.get_category_fields('cpu')
        args = request.args

        data = dict()
        for field in fields:
            if args.get(field):
                data.setdefault(field, args.get(field))

        if len(fields) == len(data) and 'id' not in args:
            utils.add_item(data, category='cpu')
        elif 'id' in args:
            data.setdefault('id', args.get('id'))
            utils.update_item(data, category='cpu')

    @api.doc(params={
        'id': 'database id to delete'
    })
    def delete(self):
        id_arg = request.args.get('id')

        if id_arg:
            utils.delete_item({'id': id_arg}, 'cpu')


@processors.route('/<id>')
class ProcessorsByID(Resource):
    @api.response(200, 'return details of a specific CPU')
    def get(self, id):
        from app.models import Processor, object_as_dict
        results = Processor.query.get(id)
        return {'cpus': object_as_dict(results)}

