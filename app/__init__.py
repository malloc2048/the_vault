from flask_restx import Api
from app.config import Config
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, title='Behold My Stuff', version='v0.1')

swagger = api.namespace(
    'categories',
    description='Behold My Stuff',
    authorizations=Config.authorizations,
    security='api_token',
    base_path='/api'
)

app.register_blueprint(blueprint=blueprint)
from app import routes, models, api_routes
