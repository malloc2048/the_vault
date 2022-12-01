from app import db


class Processor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    frequency = db.Column(db.Integer)
    socket = db.Column(db.String(128))

    display_name = 'CPUs'

    def __repr__(self):
        return f'<CPU {self.make} {self.model} {self.frequency}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('make') and data.get('model'))

