from flask import render_template, request, redirect, url_for
from app import app, models
import json


@app.route('/')
@app.route('/index')
def home():
    return render_template(
        'index.html',
        title='Home',
        categories=models.category_details(),
        category_data=[],
        category=''
    )


@app.route('/category/<category>', methods=['GET'])
def category_display(category):
    # todo separate these returns so that a db query is only done once
    attributes, data = models.get_category_data(category)

    args = request.args.to_dict()
    filtered_data = dict()
    if 'filter' in args:
        # this is just plain janky
        filter_str = args.get('filter').replace('\'', '\"')
        filter_dict = json.loads(filter_str)

    filters = dict()
    for row in data:
        for item in row:
            if item != 'id' and item != 'hash' and row[item]:
                filters.setdefault(item, set()).add(row[item])

    return render_template(
        f'category.html',
        category=category,
        attributes=attributes,
        category_data=data,
        categories=models.category_details(),
        filters=filters
    )


@app.route('/new_item/<category>', methods=['POST'])
def new_category_item(category):
    data = request.form.to_dict()

    delete = [key for key in data if data[key] in key]
    for key in delete:
        del data[key]

    if data:
        return redirect(url_for(f'category_display', category=category, filter=data))
    else:
        return redirect(url_for(f'category_display', category=category))
