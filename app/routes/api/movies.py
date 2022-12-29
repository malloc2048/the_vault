from flask import request
from app import api, video
from flask_restx import Resource
from app.models.movie import model


@video.route('/movies')
class Movies(Resource):
    @api.doc(params=model.query_fields)
    @api.response(200, 'return list of movies')
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


# @video.route('/movies/<record_id>')
# class MovieByID(Resource):
#     @api.response(200, 'return details of a specific DVD')
#     def get(self, record_id):
#         results = Movie.query.get(record_id)
#         return {'movie': object_as_dict(results)}
#
#     @api.doc(params=Movie.mutation_fields)
#     def post(self, record_id):
#         args = request.args.to_dict()
#
#         # update the record if 'id' is provided with at least one additional arg
#         if len(args) >= 1:
#             args.setdefault('id', record_id)
#             update_item(args, category='dvd', db=db)
#             return {'movie': object_as_dict(Movie.query.get(record_id))}
#
#     @api.response(200, 'return details of a specific DVD')
#     def delete(self, record_id):
#         if record_id:
#             return {'movie': object_as_dict(delete_item({'id': record_id}, 'movie', db=db))}
