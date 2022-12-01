from app import db


# can index later if things get slow
class GraphicsCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(16))
    model = db.Column(db.String(64))
    gpu_manufacturer = db.Column(db.String(8))
    gpu_series = db.Column(db.String(16))
    gpu_model = db.Column(db.String(32))
    vram = db.Column(db.String(8))
    interface = db.Column(db.String(8))

    display_name = 'GPUs'
    group = 'hardware'

    query_fields = {
        'manufacturer': 'Who made the card',
        'gpu_manufacturer': 'Who made the chip',
        'gpu_series': 'Geforce|Radeon',
        'vram': 'how much memory',
        'interface': 'How does it plug in'
    }

    mutation_fields = {
        'manufacturer': 'Who made the card',
        'model': 'card model',
        'gpu_manufacturer': 'Who made the chip',
        'gpu_series': 'Geforce|Radeon',
        'gpu_model': 'specific GPU chip model',
        'vram': 'how much memory',
        'interface': 'How does it plug in'
    }

    def __repr__(self):
        return f'<GPU {self.manufacturer} {self.model}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('gpu_manufacturer') and data.get('gpu_series') and data.get('gpu_model'))
