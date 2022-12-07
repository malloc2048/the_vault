import json
import argparse
import requests

api_url = 'http://localhost/api'


def get_api_categories() -> list:
    try:
        response = requests.get(f'{api_url}/categories')
    except requests.exceptions.ConnectionError:
        return []

    if response.status_code == 200:
        return response.json().get('categories', [])
    else:
        return []


def process_category(endpoint: str, data_items: list):
    if data_items:
        for datum in data_items:
            response = requests.post(endpoint, params=datum)
            if response.status_code != 200:
                print(f'[INFO] something went wrong status code: {response.status_code}')


def main():
    categories = get_api_categories()
    if categories:
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', type=str, required=True)
        args = parser.parse_args()

        with open(args.f) as json_data_file:
            data = json.load(json_data_file)
            endpoint = f'{api_url}/{data.get("group")}/{data.get("category")}'
            process_category(endpoint, data.get('data'))
    else:
        print('[INFO] API appears to be down')


if __name__ == '__main__':
    main()
