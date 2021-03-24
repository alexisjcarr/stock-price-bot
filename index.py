import json
import requests

from settings import URL


def handler(event, context):
    response_data = requests.get(URL, headers={"Accept": "application/json"})
    json_data = response_data.read()
    deserialized_data = json.loads(json_data)
    price = deserialized_data['price']
    return {
        'price': price,
    }
