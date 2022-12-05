from app import db


class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    socket = db.Column(db.String(128))
    status = db.Column(db.String(128))
    hash = db.Column(db.String(128), index=True)

    display_name = 'Motherboards'
    group = 'hardware'

    query_fields = {
        'make': 'who made the board',
        'socket': 'what can plug into it',
    }

    mutation_fields = {
        'make': 'who made the board',
        'model': 'specific board',
        'socket': 'what can plug into it',
        'status': 'does it work',
    }

    def __repr__(self):
        return f'<Motherboard {self.make} {self.model}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('socket'))
