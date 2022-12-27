from flask_restx import Resource
from app import api, categories, app
from app.models import category_details


# these routes ar relative to the base url (/api) and the namespace url (/categories)
# so the url path is /api/categories/
@categories.route('/')
@api.doc(params={'details': 'Show full details of the categories {True|False}'})
class Categories(Resource):
    @api.response(200, 'returns a list of all available categories')
    def get(self):
        return {'categories': category_details(False)}
