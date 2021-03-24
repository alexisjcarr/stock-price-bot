import json
from urllib.request import urlopen

from settings import URL


def handler(event, context):
    response = urlopen(URL)
    data = response.read().decode("utf-8")
    return json.loads(data)['price']
