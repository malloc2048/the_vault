from flask_restx import Api
from app.config import Config
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, title='Behold My Stuff', version='v0.1')

categories = api.namespace(
    'categories',
    description='The categories I track',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

processors = api.namespace(
    'processors',
    description='The CPUs I gots',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

motherboards = api.namespace(
    'motherboards',
    description='The motherboards I gots',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

operating_systems = api.namespace(
    'operating_systems',
    description='The operating systems I gots',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

app.register_blueprint(blueprint=blueprint)
from app import routes, models
from app.api_routes import processor, categories, motherboards, operating_systems
