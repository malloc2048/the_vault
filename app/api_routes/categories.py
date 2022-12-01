from flask import request
from flask_restx import Resource
from app import api, categories, processors, models


# these routes ar relative to the base url (/api) and the namespace url (/categories)
# so the url path is /api/categories/
@categories.route('/')
@api.doc(params={'details': 'Show full details of the categories {True|False}'})
class Categories(Resource):
    @api.response(200, 'returns a list of all available categories')
    def get(self):
        args = request.args
        show_details = bool(args.get('details'))
        return {'categories': models.category_details(show_details)}
