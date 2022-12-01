from app import db


class DVD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    format = db.Column(db.String(128), index=True)
    director = db.Column(db.String(128), index=True)
    release = db.Column(db.String(128), index=True)

    display_name = 'DVDs'

    def __repr__(self):
        return f'<DVD {self.title}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'format': self.format,
            'release': self.release,
        }

    @staticmethod
    def field_names() -> list:
        # so if this order is changed the display on the page is wrong, format for director and vise versa
        # why?
        return ['title', 'director', 'format', 'release']

    @staticmethod
    def display_names() -> list:
        names = DVD.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict) -> bool:
        self.title = data.get('title') if data.get('title') else self.title
        self.director = data.get('director') if data.get('director') else self.director
        self.format = data.get('format') if data.get('format') else self.format
        self.release = data.get('release') if data.get('release') else self.release

        return True
