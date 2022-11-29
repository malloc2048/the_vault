from sqlalchemy import inspect
from app import db


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


class GraphicsCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(120), index=True)
    vram = db.Column(db.Integer)
    interface = db.Column(db.String(120))

    def __repr__(self):
        return f'<GPU {self.make} {self.model}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'vram': self.vram,
            'interface': self.interface
        }

    @staticmethod
    def field_names() -> list:
        return ['make', 'model', 'vram', 'interface']

    @staticmethod
    def display_names() -> list:
        names = GraphicsCard.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('make') if data.get('make') else self.make
        self.model = data.get('model') if data.get('model') else self.model
        self.socket = data.get('vram') if data.get('vram') else self.socket
        self.frequency = data.get('interface') if data.get('interface') else self.frequency

        return True


class Processor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    frequency = db.Column(db.Integer)
    socket = db.Column(db.String(128))

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


class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True)
    socket = db.Column(db.String(128))
    status = db.Column(db.String(128))

    def __repr__(self):
        return f'<Motherboard {self.make} {self.model}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'socket': self.socket,
            'status': self.status
        }

    @staticmethod
    def field_names() -> list:
        return ['make', 'model', 'socket', 'status']

    @staticmethod
    def display_names() -> list:
        names = Motherboard.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('make') if data.get('make') else self.make
        self.model = data.get('model') if data.get('model') else self.model
        self.socket = data.get('socket') if data.get('socket') else self.socket
        self.status = data.get('status') if data.get('status') else self.status

        return True


class OS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    version = db.Column(db.String(128))
    media_type = db.Column(db.String(128))
    product_key = db.Column(db.String(128))

    def __repr__(self):
        return f'<OS {self.publisher} {self.name}>'

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'publisher': self.publisher,
            'name': self.name,
            'version': self.version,
            'key': self.product_key,
            'media_type': self.media_type
        }

    @staticmethod
    def field_names() -> list:
        return ['publisher', 'name', 'version', 'product Key', 'media type']

    @staticmethod
    def required_field_names() -> list:
        return ['publisher', 'name', 'version']

    @staticmethod
    def display_names() -> list:
        names = OS.field_names()
        names.insert(0, 'id')
        return names

    def from_dict(self, data: dict):
        self.publisher = data.get('publisher') if data.get('publisher') else self.publisher
        self.name = data.get('name') if data.get('name') else self.name
        self.version = data.get('version') if data.get('version') else self.version
        self.media_type = data.get('media type') if data.get('media type') else self.media_type
        self.product_key = data.get('product Key') if data.get('product Key') else self.product_key

        return True
