from flask import render_template, request, redirect
from app import app, utils


@app.route('/')
@app.route('/index')
def home():
    return render_template(
        'index.html',
        title='Home',
        categories=utils.categories(),
        category_data=[],
    )


@app.route('/category/<category>', methods=['GET', 'POST'])
def category_display(category):
    if request.method == 'GET':
        attributes, data = utils.get_category_data(category)
        display_name = utils.get_category_display_name(category)

        return render_template(
            f'category.html',
            category_display_name=display_name,
            category=category,
            attributes=attributes,
            category_data=data,
            categories=utils.categories(),
        )

    elif request.method == 'POST':
        print('ever here?')


@app.route('/new_item/<category>', methods=['POST'])
def new_category_item(category):
    try:
        data = request.form.to_dict()

        if data.get('ID'):
            update = False

            # if any other field is populated other than ID, then update the entry, otherwise we are gonna delete
            for x in data:
                if x != 'ID' and data.get(x):
                    update = True

            if update:
                utils.update_item(data, category)
            else:
                utils.delete_item(data, category)

        else:
            utils.add_item(data, category)

    except KeyError:
        pass
    return redirect(f'/category/{category}')
