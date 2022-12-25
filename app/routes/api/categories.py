import json
import hashlib
from flask_restx import Resource
from app import api, categories, app, models, db


# these routes ar relative to the base url (/api) and the namespace url (/categories)
# so the url path is /api/categories/
@categories.route('/')
@api.doc(params={'details': 'Show full details of the categories {True|False}'})
class Categories(Resource):
    @api.response(200, 'returns a list of all available categories')
    def get(self):
        api_routes = set()
        for rule in app.url_map.iter_rules():
            api_route = rule.__str__()
            if 'api' in api_route:
                route_pieces = api_route.split('/')
                if route_pieces[2] and 'swagger' not in route_pieces[2]:
                    if route_pieces[3]:
                        api_routes.add(f'{route_pieces[2]}/{route_pieces[3]}')
        return {'categories': list(api_routes)}
