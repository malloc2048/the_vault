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
    mutation_fields={
        'title': 'video title',
        'format': 'video format [DVD|Blu-Ray|MP4]',
        'director': 'who made it',
        'release': 'when did they make it'
    }
)
