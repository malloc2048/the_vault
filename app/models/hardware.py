from app.models.model import Model


model = Model(
    display_name='Hardware',
    display_fields=[
        'type',
        'manufacturer',
        'model'
    ],
    query_fields={
        'type': '',
        'manufacturer': '',
        'model': ''
    }
)
