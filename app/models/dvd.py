from app import db


class DVD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    release_date = db.Column(db.String(128), index=True)
    director = db.Column(db.String(128), index=True)

    display_name = 'DVDs'

    def __repr__(self):
        return f'<DVD {self.title}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'director': self.director
        }

    @staticmethod
    def field_names() -> list:
        return ['title', 'release_date', 'director']

    @staticmethod
    def display_names() -> list:
        names = DVD.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict) -> bool:
        self.title = data.get('title') if data.get('title') else self.make
        self.director = data.get('director') if data.get('director') else self.model
        self.release_date = data.get('release_date') if data.get('release_date') else self.socket

        return True
