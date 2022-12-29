from flask import request
from app import api, software
from flask_restx import Resource
from app.models.game import model


@software.route('/games')
class Games(Resource):
    @api.doc(params=model.query_fields)
    @api.response(200, 'returns a list of games')
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


# @software.route('/games/<record_id>')
# class GamesById(Resource):
#     @api.response(200, 'return details of a specific operating system')
#     def get(self, record_id):
#         results = Game.query.get(record_id)
#         return {'game': object_as_dict(results)}
#
#     @api.doc(params=Game.mutation_fields)
#     @api.response(200, 'updated operating system record')
#     def post(self, record_id):
#         args = request.args.to_dict()
#
#         # update the record if 'id' is provided with at least one additional arg
#         if len(args) >= 1:
#             args.setdefault('id', record_id)
#             update_item(args, category='game', db=db)
#             return {'game': object_as_dict(Game.query.get(record_id))}
#
#     @api.response(200, 'return deleted operating system record')
#     def delete(self, record_id):
#         if record_id:
#             return {'game': object_as_dict(delete_item({'id': record_id}, 'game', db=db))}
