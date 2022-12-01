from flask import render_template, request, redirect, url_for
from app import app, models, db


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
    if request.method == 'GET':
        print(request.args.to_dict())

        attributes, data = models.get_category_data(category)
        attributes.remove('id')
        print(data)

        return render_template(
            f'category.html',
            category_display_name=models.get_category_display_name(category),
            category=category,
            attributes=attributes,
            category_data=data,
            categories=models.category_details(),
        )


@app.route('/new_item/<category>', methods=['POST'])
def new_category_item(category):
    try:
        data = request.form.to_dict()

        if data.get('id'):
            update = False

            # if any other field is populated other than ID, then update the entry, otherwise we are going to delete
            for x in data:
                if x != 'id' and data.get(x):
                    update = True

            if update:
                models.update_item(data, category, db)
            else:
                models.delete_item(data, category, db)

        else:
            models.add_item(data, category, db)

    except KeyError:
        pass
    return redirect(url_for(f'/category/{category}', filter='filter'))
