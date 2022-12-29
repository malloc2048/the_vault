from flask import request
from app import api, software
from flask_restx import Resource
from app.models.software import model


@software.route('/operating_systems')
class OperatingSystem(Resource):
    @api.doc(params=model.query_fields)
    @api.response(200, 'return list of operating systems')
    def get(self):
        args = request.args.to_dict()
        if args:
            return model.query(args)
        return model.query()

    @api.doc(params=model.mutation_fields)
    def post(self):
        args = request.args.to_dict()

        if model.validate(args):
            _, record = model.add(args)
            return record

        else:
            return dict()


# @software.route('/operating_systems/<id>')
# class OperatingSystemById(Resource):
#     @api.response(200, 'return details of a specific operating system')
#     def get(self, record_id):
#         results = OS.query.get(record_id)
#         return {'operating system': object_as_dict(results)}
#
#     @api.doc(params=OS.mutation_fields)
#     @api.response(200, 'updated operating system record')
#     def post(self, record_id):
#         args = request.args.to_dict()
#
#         # update the record if 'id' is provided with at least one additional arg
#         if len(args) >= 1:
#             args.setdefault('id', record_id)
#             update_item(args, category='os', db=db)
#             return {'operating system': object_as_dict(OS.query.get(record_id))}
#
#     @api.response(200, 'return deleted operating system record')
#     def delete(self, record_id):
#         if record_id:
#             return {'operating system': object_as_dict(delete_item({'id': record_id}, 'os', db=db))}
