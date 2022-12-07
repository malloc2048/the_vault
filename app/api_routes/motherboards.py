from flask import request
from flask_restx import Resource
from app import api, hardware, db
from app.utils import object_as_dict
from app.api_routes import category_get
from app.models import add_item, update_item, delete_item, Motherboard


@hardware.route('/motherboard')
class Motherboards(Resource):
    @api.doc(params=Motherboard.query_fields)
    @api.response(200, 'returns a list of all motherboards')
    def get(self):
            args = request.args.to_dict()
            return category_get(args, 'mb')

    @api.doc(params=Motherboard.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if Motherboard.validate(args):
            return object_as_dict(add_item(data=args, category='mb', db=db))


@hardware.route('/motherboard/<record_id>')
class MotherboardsById(Resource):
    @api.response(200, 'return details of a specific motherboard')
    def get(self, record_id):
        results = Motherboard.query.get(record_id)
        return {'motherboard': object_as_dict(results)}

    @api.doc(params=Motherboard.mutation_fields)
    @api.response(200, 'updated motherboard record')
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='mb', db=db)
            return {'motherboard': object_as_dict(Motherboard.query.get(record_id))}

    @api.response(200, 'return deleted motherboard record')
    def delete(self, record_id):
        if record_id:
            return {'motherboard': object_as_dict(delete_item({'id': record_id}, 'mb', db=db))}
