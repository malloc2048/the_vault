def filter_data(filters: list, data: list) -> list:
    keep_data = list()
    for datum in data:
        for filter in filters:
            if filter in datum.values():
                keep_data.append(datum)
    return keep_data
