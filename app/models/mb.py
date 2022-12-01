from app import db


class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    socket = db.Column(db.String(128))
    status = db.Column(db.String(128))

    display_name = 'Motherboards'

    def __repr__(self):
        return f'<Motherboard {self.make} {self.model}>'

    @staticmethod
    def field_names() -> list:
        return ['make', 'model', 'socket', 'status']

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('make') if data.get('make') else self.make
        self.model = data.get('model') if data.get('model') else self.model
        self.socket = data.get('socket') if data.get('socket') else self.socket
        self.status = data.get('status') if data.get('status') else self.status

        return True
