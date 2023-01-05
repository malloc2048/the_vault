from app.models.model import Model


model = Model(
    display_name='Hardware',
    display_fields=[
        'type',
        'manufacturer',
        'model'
    ],
    query_fields={
        'type': 'the hardware type',
        'manufacturer': 'who made it',
        'model': 'what they called it'
    },
    mutation_fields={
        'manufacturer': 'who made it',
        'model': 'what they called it'
    }
)
