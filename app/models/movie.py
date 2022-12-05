from app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    format = db.Column(db.String(128), index=True)
    director = db.Column(db.String(128), index=True)
    release = db.Column(db.String(4), index=True)
    hash = db.Column(db.String(128), index=True)

    display_name = 'Movies'
    group = 'media'

    query_fields = {
        'format': 'what media type is it on',
        'director': 'who directed it',
        'release': 'when was it released',
    }

    mutation_fields = {
        'title': 'what is it called',
        'format': 'what media type is it on',
        'director': 'who directed it',
        'release': 'when was it released',
    }

    def __repr__(self):
        return f'<Movie {self.title}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('title'))
