from app.models.model import Model


model = Model(
    display_name='Software',
    display_fields=[
        'publisher',
        'name',
        'version'
    ],
    query_fields={}
)
