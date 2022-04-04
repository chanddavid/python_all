

import json
import requests

URL = "http://127.0.0.1:8000/getdata/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)

    data = r.json()
    print(data)
# get_data()


def post_data():
    data = {
        'name': 'ankmn',
        'roll': 10,
        'city': 'xaina'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)
post_data()


def update_data():
    data = {
        'id': 5,
        'name': 'samm',
        'roll': 390,
        'city': 'pokhara'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)
# update_data()


def partial_data():
    data = {
        'id': 5,
        'name': 'sammar',
        'roll': 390,
        'city': 'pokhara'
    }
    json_data = json.dumps(data)
    r = requests.patch(url=URL, data=json_data)

    data = r.json()
    print(data)
# partial_data()

def delete_data():
    data = {
        'id': 5,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)

    data = r.json()
    print(data)
# delete_data()

