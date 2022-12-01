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

    def __repr__(self):
        return f'<GPU {self.manufacturer} {self.model}>'

    @staticmethod
    def validate(data: dict) -> bool:
        return bool(data.get('gpu_manufacturer') and data.get('gpu_series') and data.get('gpu_model'))
