from app import db


class GraphicsCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(120), index=True, unique=True)
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
        return ['Make', 'Model', 'VRAM', 'Interface']

    @staticmethod
    def display_names() -> list:
        names = GraphicsCard.field_names()
        names.insert(0, 'ID')
        return names

    def from_dict(self, data: dict) -> bool:
        for attribute in self.field_names():
            if not data.get(attribute):
                return False

        self.make = data.get('make')
        self.vram = data.get('vram')
        self.model = data.get('model')
        self.interface = data.get('interface')

        return True


class Processor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True, unique=True)
    frequency = db.Column(db.Integer)
    socket = db.Column(db.String(128))

    def __repr__(self):
        return f'<CPU {self.make} {self.model}>'

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
        return ['Make', 'Model', 'Frequency', 'Socket']

    @staticmethod
    def display_names() -> list:
        names = Processor.field_names()
        names.insert(0, 'ID')
        return names

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('Make') if data.get('Make') else self.make
        self.model = data.get('Model') if data.get('Model') else self.model
        self.socket = data.get('Socket') if data.get('Socket') else self.socket
        self.frequency = data.get('Frequency') if data.get('Frequency') else self.frequency

        return True


class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), index=True)
    model = db.Column(db.String(128), index=True, unique=True)
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
        return ['Make', 'Model', 'Socket', 'Status']

    @staticmethod
    def display_names() -> list:
        names = Motherboard.field_names()
        names.insert(0, 'ID')
        return names

    def from_dict(self, data: dict) -> bool:
        self.make = data.get('Make') if data.get('Make') else self.make
        self.model = data.get('Model') if data.get('Model') else self.model
        self.socket = data.get('Socket') if data.get('Socket') else self.socket
        self.status = data.get('Status') if data.get('Status') else self.status

        return True


class OS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True, unique=True)
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
        return ['Publisher', 'Name', 'Version', 'Product Key', 'Media Type']

    @staticmethod
    def display_names() -> list:
        names = OS.field_names()
        names.insert(0, 'ID')
        return names

    def from_dict(self, data: dict):
        self.publisher = data.get('Make') if data.get('Make') else self.publisher
        self.name = data.get('Name') if data.get('Name') else self.name
        self.version = data.get('Version') if data.get('Version') else self.version
        self.media_type = data.get('Media Type') if data.get('Media Type') else self.media_type
        self.product_key = data.get('Product Key') if data.get('Product Key') else self.product_key

        return True
