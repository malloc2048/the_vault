from app import db


class GraphicsCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(120), index=True)
    vram = db.Column(db.Integer)
    interface = db.Column(db.String(120))

    display_name = 'GPUs'

    def __repr__(self):
        return f'<GPU {self.make} {self.model}>'

    @staticmethod
    def field_names() -> list:
        return ['make', 'model', 'vram', 'interface']

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('make') if data.get('make') else self.make
        self.model = data.get('model') if data.get('model') else self.model
        self.socket = data.get('vram') if data.get('vram') else self.socket
        self.frequency = data.get('interface') if data.get('interface') else self.frequency

        return True
