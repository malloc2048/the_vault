import json
import argparse
import requests

api_url = 'http://localhost/api/'


def get_api_categories() -> list:
    try:
        response = requests.get(f'{api_url}/categories')
    except requests.exceptions.ConnectionError:
        return []

    if response.status_code == 200:
        return response.json().get('categories', [])
    else:
        return []


def process_category(category: str, data_items: list):
    if data_items:
        endpoint = f'{api_url}{category}'

        for datum in data_items:
            response = requests.post(endpoint, params=datum)
            if response.status_code != 200:
                print(f'[INFO] something went wrong status code: {response.status_code}')


def dedup():
    endpoint = f'{api_url}categories/dedup'
    response = requests.get(endpoint)
    if response.status_code != 200:
        print(f'[INFO] something went wrong deduping status code: {response.status_code}')


def main():
    categories = get_api_categories()
    if categories:
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', type=str, required=True)
        args = parser.parse_args()

        with open(args.f) as json_data_file:
            data = json.load(json_data_file)

            for category in categories:
                process_category(category, data.get(category))
        dedup()
    else:
        print('[INFO] API appears to be down')


if __name__ == '__main__':
    main()
