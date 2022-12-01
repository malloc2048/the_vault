from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    release = db.Column(db.String(128), index=True)
    platform = db.Column(db.String(8), index=True)
    publisher = db.Column(db.String(128), index=True)

    display_name = 'Games'

    def __repr__(self):
        return f'<Game {self.title} {self.platform}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('title') and data.get('platform'))
