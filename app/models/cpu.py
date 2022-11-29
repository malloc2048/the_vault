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

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'frequency': self.frequency,
            'socket': self.socket
        }

    @staticmethod
    def field_names() -> list:
        return ['make', 'model', 'frequency', 'socket']

    @staticmethod
    def display_names() -> list:
        names = Processor.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('make') if data.get('make') else self.make
        self.model = data.get('model') if data.get('model') else self.model
        self.socket = data.get('socket') if data.get('socket') else self.socket
        self.frequency = data.get('frequency') if data.get('frequency') else self.frequency

        return True
