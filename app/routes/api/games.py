from flask import request
from flask_restx import Resource
from app import api, software, db
from app.utils import object_as_dict
from app.routes.api import category_get
from app.models import add_item, update_item, delete_item, Game


@software.route('/games')
class Games(Resource):
    @api.doc(params=Game.query_fields)
    @api.response(200, 'returns a list of operating systems')
    def get(self):
        args = request.args.to_dict()
        return category_get(args, 'game')

    @api.doc(params=Game.mutation_fields)
    def post(self):
        # fields = get_category_fields('dvd')
        args = request.args.to_dict()

        # validate title at least is provided
        if Game.validate(args):
            return object_as_dict(add_item(data=args, category='game', db=db))


@software.route('/games/<record_id>')
class GamesById(Resource):
    @api.response(200, 'return details of a specific operating system')
    def get(self, record_id):
        results = Game.query.get(record_id)
        return {'game': object_as_dict(results)}

    @api.doc(params=Game.mutation_fields)
    @api.response(200, 'updated operating system record')
    def post(self, record_id):
        args = request.args.to_dict()

        # update the record if 'id' is provided with at least one additional arg
        if len(args) >= 1:
            args.setdefault('id', record_id)
            update_item(args, category='game', db=db)
            return {'game': object_as_dict(Game.query.get(record_id))}

    @api.response(200, 'return deleted operating system record')
    def delete(self, record_id):
        if record_id:
            return {'game': object_as_dict(delete_item({'id': record_id}, 'game', db=db))}
