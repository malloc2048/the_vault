from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    release = db.Column(db.String(4), index=True)
    platform = db.Column(db.String(8), index=True)
    developer = db.Column(db.String(128), index=True)
    genre = db.Column(db.String(16), index=True)

    display_name = 'Games'
    group = 'software'

    query_fields = {
        'release': 'what year was it released',
        'platform': 'what hardware does it run on',
        'publisher': 'who made it',
    }

    mutation_fields = {
        'title': 'what is it called',
        'release': 'what year was it released',
        'platform': 'what hardware does it run on',
        'publisher': 'who made it',
    }

    def __repr__(self):
        return f'<Game {self.title} {self.platform}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('title') and data.get('platform'))
