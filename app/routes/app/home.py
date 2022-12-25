from app import app
from flask import render_template
from app.models.utils import category_details


@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Home',
        categories=category_details(),
        category_data=[],
        category=''
    )
