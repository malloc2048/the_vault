from flask import request
from flask_restx import Resource
from app import api, processors, db
from app.utils import object_as_dict
from app.api_routes import category_get
from app.models import add_item, update_item, delete_item, Processor


@processors.route('/')
class Processors(Resource):
    @api.doc(params=Processor.query_fields)
    @api.response(200, 'returns a list of cpus')
    def get(self):
        args = request.args.to_dict()
        return category_get(args, 'cpu')

    @api.doc(params=Processor.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if Processor.validate(args):
            return object_as_dict(add_item(data=args, category='cpu', db=db))


@processors.route('/<id>')
class ProcessorsByID(Resource):
    @api.response(200, 'return details of a specific cpu')
    def get(self, record_id):
        results = Processor.query.get(record_id)
        return {'cpus': object_as_dict(results)}

    @api.doc(params=Processor.mutation_fields)
    @api.response(200, 'updated cpu record')
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='cpu', db=db)
            return {'cpus': object_as_dict(Processor.query.get(record_id))}

    @api.response(200, 'return deleted cpu record')
    def delete(self, record_id):
        if record_id:
            return {'movie': object_as_dict(delete_item({'id': record_id}, 'cpu', db=db))}
