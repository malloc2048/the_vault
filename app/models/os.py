from app import db


class OS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(16), index=True)
    name = db.Column(db.String(16), index=True)
    version = db.Column(db.String(16))
    software_version = db.Column(db.String(16))
    product_key = db.Column(db.String(32))

    display_name = 'Operating Systems'
    group = 'software'

    query_fields = {
        'publisher': 'what is it called',

    }

    mutation_fields = {
        'publisher': 'who made it',
        'name': 'what it is called (pos does not count)',
        'version': 'common known version (think 95 in Windows 95)',
        'software_version': 'detail version number if known',
        'product_key': 'product key if there is one',
    }

    def __repr__(self):
        return f'<OS {self.publisher} {self.name}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('publisher') and data.get('name') and data.get('version'))
