from .model import Model


model = Model(
    display_name='Videos',
    display_fields=[
        'title',
        'format',
        'director',
        'release'
    ],
    query_fields={},
    mutation_fields={}
)
