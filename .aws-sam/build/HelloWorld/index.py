from urllib.request import urlopen
from contextlib import closing
import json

from constants import URL


def handler(event, context):
    with closing(urlopen(URL)) as response_data:
        json_data = response_data.read()
        deserialized_data = json.loads(json_data)
        price = deserialized_data['price']
    return {
        'price': price,
        'base64Encoded': False
    }
