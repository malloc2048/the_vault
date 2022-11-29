import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-have-to-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'my_stuff.sqlit3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    authorizations = {
        'api_token': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'x-auth'
        }
    }
