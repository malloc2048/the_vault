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


def filter_data(filters: list, data: list) -> list:
    keep_data = list()
    for datum in data:
        for filter in filters:
            if filter in datum.values():
                keep_data.append(datum)
    return keep_data


@app.route('/category/<category>', methods=['GET'])
def category_display(category):
    # todo separate these returns so that a db query is only done once
    attributes, data = models.get_category_data(category)

    # convert the requested filters if present
    args = request.args.to_dict()
    filter_dict = dict()
    if 'filter' in args:
        # this is just plain janky
        filter_str = args.get('filter').replace('\'', '\"')
        filter_dict = json.loads(filter_str)

    # this is how I am getting what is displayed as a possible filter
    filters = dict()
    for row in data:
        for item in row:
            if item != 'id' and item != 'hash' and row[item]:
                filters.setdefault(item, set()).add(row[item])

    # filter the results
    if filter_dict:
        data = filter_data(list(filter_dict.values()), data)

    return render_template(
        f'category.html',
        category=category,
        attributes=attributes,
        category_data=data,
        categories=models.category_details(),
        filters=filters
    )


@app.route('/filter/<category>', methods=['POST'])
def new_category_item(category):
    data = request.form.to_dict()

    delete = [key for key in data if data[key] in key]
    for key in delete:
        del data[key]

    if data:
        return redirect(url_for(f'category_display', category=category, filter=data))
    else:
        return redirect(url_for(f'category_display', category=category))
