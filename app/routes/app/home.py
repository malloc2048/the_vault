from app import app
from flask import render_template
from app.models import category_details, load_data_files


@app.route('/')
def home():
    load_data_files()
    return render_template(
        'index.html',
        title='Home',
        categories=category_details(),
        category_data=[],
        category=''
    )
