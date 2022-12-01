from flask import request
from flask_restx import Resource
from app.utils import object_as_dict
from app.api_routes import category_get
from app import api, operating_systems, db
from app.models import add_item, update_item, delete_item, OS


@operating_systems.route('/')
class Motherboards(Resource):
    @api.doc(params=OS.query_fields)
    @api.response(200, 'returns a list of operating systems')
    def get(self):
        args = request.args.to_dict()
        return category_get(args, 'os')

    @api.doc(params=OS.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if OS.validate(args):
            return object_as_dict(add_item(data=args, category='os', db=db))


@operating_systems.route('/<id>')
class MotherboardsById(Resource):
    @api.response(200, 'return details of a specific operating system')
    def get(self, record_id):
        results = OS.query.get(record_id)
        return {'oss': object_as_dict(results)}

    @api.doc(params=OS.mutation_fields)
    @api.response(200, 'updated operating system record')
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='os', db=db)
            return {'oss': object_as_dict(OS.query.get(record_id))}

    @api.response(200, 'return deleted operating system record')
    def delete(self, record_id):
        if record_id:
            return {'movie': object_as_dict(delete_item({'id': record_id}, 'os', db=db))}
