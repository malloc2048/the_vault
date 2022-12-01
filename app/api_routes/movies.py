from flask import request
from app import api, movies, db
from flask_restx import Resource
from app.utils import object_as_dict
from app.models import get_category_data, get_category_fields, add_item, update_item, delete_item, Movie


@movies.route('/')
class Movies(Resource):
    @api.doc(params={
        'format': 'media type',
        'director': 'who made it',
        'release': 'when was it made',
    })
    @api.response(200, 'returns a list of all available processors')
    def get(self):
        args = request.args

        filter_data = dict()
        if args.get('title'):
            filter_data.setdefault('title', args.get('title'))
        if args.get('director'):
            filter_data.setdefault('director', args.get('director'))
        if args.get('release_date'):
            filter_data.setdefault('release_date', args.get('release_date'))

        all_data = get_category_data('dvd')[1]
        if not filter_data:
            return {'dvds': all_data}
        else:
            filtered_data = list()
            for item in all_data:
                shared_items = {k: filter_data[k] for k in filter_data if k in item and filter_data[k] == item[k]}
                if len(shared_items) == len(filter_data):
                    filtered_data.append(item)
            return {'dvds': filtered_data}

    @api.doc(params={
        'title': 'what did they call it',
        'director': 'who made the movie',
        'format': 'how is it packaged',
        'release': 'when did they release it',
    })
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if args.get('title'):
            return object_as_dict(add_item(data=args, category='dvd', db=db))


@movies.route('/<record_id>')
class MovieByID(Resource):
    @api.response(200, 'return details of a specific DVD')
    def get(self, record_id):
        results = Movie.query.get(record_id)
        return {'movie': object_as_dict(results)}

    @api.doc(params={
        'title': 'what did they call it',
        'director': 'who made the movie',
        'format': 'how is it packaged',
        'release': 'when did they release it',
    })
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
            return {'movie': object_as_dict(delete_item({'id': record_id}, 'dvd', db=db))}
