from flask import request
from flask_restx import Resource
from app import api, hardware, db
from app.utils import object_as_dict
from app.routes.api import category_get
from app.models import add_item, update_item, delete_item, GraphicsCard


@hardware.route('/gpu')
class Gpus(Resource):
    @api.doc(params=GraphicsCard.query_fields)
    @api.response(200, 'returns a list of graphics cards')
    def get(self):
        args = request.args.to_dict()
        return category_get(args, 'gpu')

    @api.doc(params=GraphicsCard.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if GraphicsCard.validate(args):
            return object_as_dict(add_item(data=args, category='gpu', db=db))


@hardware.route('/gpu/<record_id>')
class GpuByID(Resource):
    @api.response(200, 'return details of a specific gpu')
    def get(self, record_id):
        results = GraphicsCard.query.get(record_id)
        return {'gpu': object_as_dict(results)}

    @api.doc(params=GraphicsCard.mutation_fields)
    @api.response(200, 'updated gpu record')
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='gpu', db=db)
            return {'gpu': object_as_dict(GraphicsCard.query.get(record_id))}

    @api.response(200, 'return deleted gpu record')
    def delete(self, record_id):
        if record_id:
            return {'gpu': object_as_dict(delete_item({'id': record_id}, 'gpu', db=db))}

