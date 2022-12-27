from flask import request
from app import api, hardware
from flask_restx import Resource
from app.models.hardware import model
from app.routes.api import category_get


@hardware.route('/hardware')
class Hardware(Resource):
    @api.doc(params=model.query_fields)
    @api.response(200, 'returns a list of all hardware')
    def get(self):
        args = request.args.to_dict()
        return model.query_all()
        # return category_get(args, 'mb')

    # @api.doc(params=Motherboard.mutation_fields)
    # def post(self):
    #     # fields = get_category_fields('dvd')
    #     args = request.args.to_dict()
    #
    #     # validate title at least is provided
    #     if Motherboard.validate(args):
    #         return object_as_dict(add_item(data=args, category='mb', db=db))


# @hardware.route('/hardware/<record_id>')
# class MotherboardsById(Resource):
#     @api.response(200, 'return details of a specific motherboard')
#     def get(self, record_id):
#         results = Motherboard.query.get(record_id)
#         return {'motherboard': object_as_dict(results)}
#
#     @api.doc(params=Motherboard.mutation_fields)
#     @api.response(200, 'updated motherboard record')
#     def post(self, record_id):
#         args = request.args.to_dict()
#
#         # update the record if 'id' is provided with at least one additional arg
#         if len(args) >= 1:
#             args.setdefault('id', record_id)
#             update_item(args, category='mb', db=db)
#             return {'motherboard': object_as_dict(Motherboard.query.get(record_id))}
#
#     @api.response(200, 'return deleted motherboard record')
#     def delete(self, record_id):
#         if record_id:
#             return {'motherboard': object_as_dict(delete_item({'id': record_id}, 'mb', db=db))}
