from flask_restx import Api
from app.config import Config
from flask import Flask, Blueprint
from app.models import load_data_files
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, title='Behold My Stuff', version='v0.1')

categories = api.namespace(
    'categories',
    description='The categories I track',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

hardware = api.namespace(
    'hardware',
    description='The hardware group',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

software = api.namespace(
    'software',
    description='The software group',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

video = api.namespace(
    'videos',
    description='The video group',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

from app.routes.app import home, category

load_data_files()
app.register_blueprint(blueprint=blueprint)

