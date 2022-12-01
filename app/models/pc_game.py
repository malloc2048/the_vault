from app import db


class PCGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    format = db.Column(db.String(128), index=True)
    director = db.Column(db.String(128), index=True)
    release = db.Column(db.String(128), index=True)

    display_name = 'PC Games'

    def __repr__(self):
        return f'<PC Game {self.title}>'

    @staticmethod
    def field_names() -> list:
        # so if this order is changed the display on the page is wrong, format for director and vise versa
        # why?
        return ['title', 'director', 'format', 'release']

    def from_dict(self, data: dict) -> bool:
        self.title = data.get('title') if data.get('title') else self.title
        self.director = data.get('director') if data.get('director') else self.director
        self.format = data.get('format') if data.get('format') else self.format
        self.release = data.get('release') if data.get('release') else self.release

        return True
