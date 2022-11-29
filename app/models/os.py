from app import db


class OS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    version = db.Column(db.String(128))
    media_type = db.Column(db.String(128))
    product_key = db.Column(db.String(128))

    display_name = 'Operating Systems'

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
        return ['publisher', 'name', 'version', 'product key', 'media']

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
        self.media_type = data.get('media') if data.get('media') else self.media_type
        self.product_key = data.get('product Key') if data.get('product Key') else self.product_key

        return True
