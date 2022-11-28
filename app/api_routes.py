from flask import request
from flask_restx import Resource
from app import api, swagger, utils


# these routes ar relative to the base url (/api) and the namespace url (/categories)
# so the url path is /api/categories/
@swagger.route('/')
@api.doc(params={'details': 'Show full details of the categories {True|False}'})
class Categories(Resource):
    @api.response(200, 'returns a list of all available categories')
    def get(self):
        args = request.args
        show_details = bool(args.get('details'))
        return {'categories': utils.categories(show_details)}
