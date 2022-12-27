from app.models.model import Model


model = Model(
    display_name='Games',
    display_fields=[
        'title',
        'platform',
        'publisher',
        'genre'
    ],
    query_fields={}
)
