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
                    api_routes.add(route_pieces[2])

        return {'categories': list(api_routes)}


@categories.route('/dedup')
class DeDuplicateCategories(Resource):
    def get(self):
        categories = models.category_details(False)
        seen_hashes = list()

        for category in categories:
            _, cat_data = models.get_category_data(category)
            for entry in cat_data:
                entry_id = entry.pop('id')
                entry_hash = hashlib.sha256(json.dumps(entry).encode('utf-8'))
                if entry_hash.hexdigest() in seen_hashes:
                    models.delete_item({'id': entry_id}, category, db)
                else:
                    seen_hashes.append(entry_hash.hexdigest())
        return {'categories': categories}
