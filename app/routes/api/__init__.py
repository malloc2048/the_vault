from app.models import get_category_data, get_category_display_name


def category_get(args: dict, category: str):
    filter_data = dict()

    for arg in args:
        filter_data.setdefault(arg, args.get(arg))
    all_data = get_category_data(category)[1]

    display_name = get_category_display_name(category).lower()
    if not filter_data:
        return {display_name: all_data}
    else:
        filtered_data = list()
        for item in all_data:
            shared_items = {k: filter_data[k] for k in filter_data if k in item and filter_data[k] == item[k]}
            if len(shared_items) == len(filter_data):
                filtered_data.append(item)
        return {display_name: filtered_data}

