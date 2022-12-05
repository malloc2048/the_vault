from app import db


class Processor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    frequency = db.Column(db.Integer)
    socket = db.Column(db.String(128))
    hash = db.Column(db.String(128), index=True)

    display_name = 'CPUs'
    group = 'hardware'

    query_fields = {
        'make': 'Who made the cpu',
        'model': 'cpu model',
        'frequency': 'how fast is it',
        'socket': 'what does it plug into',
    }

    mutation_fields = {
        'make': 'Who made the cpu',
        'model': 'cpu model',
        'frequency': 'how fast is it',
        'socket': 'what does it plug into',
    }

    def __repr__(self):
        return f'<CPU {self.make} {self.model} {self.frequency}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('make') and data.get('model'))

