from flask import request
from app import api, video, db
from flask_restx import Resource
from app.utils import object_as_dict
from app.api_routes import category_get
from app.models import add_item, update_item, delete_item, Movie


@video.route('/movies')
class Movies(Resource):
    @api.doc(params=Movie.query_fields)
    @api.response(200, 'return list of movies')
    def get(self):
        args = request.args.to_dict()
        return category_get(args, 'movie')

    @api.doc(params=Movie.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if Movie.validate(args):
            return object_as_dict(add_item(data=args, category='movie', db=db))


@video.route('/movies/<record_id>')
class MovieByID(Resource):
    @api.response(200, 'return details of a specific DVD')
    def get(self, record_id):
        results = Movie.query.get(record_id)
        return {'movie': object_as_dict(results)}

    @api.doc(params=Movie.mutation_fields)
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='dvd', db=db)
            return {'movie': object_as_dict(Movie.query.get(record_id))}

    @api.response(200, 'return details of a specific DVD')
    def delete(self, record_id):
        if record_id:
            return {'movie': object_as_dict(delete_item({'id': record_id}, 'movie', db=db))}
