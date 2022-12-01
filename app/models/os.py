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

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('publisher') and data.get('name') and data.get('version'))
