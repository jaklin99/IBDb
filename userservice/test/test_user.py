import requests
import string
import random
from config import config

username = None
password = None
token = None


def test_post_users():
    global username
    global password
    username = ''.join(random.sample(string.ascii_letters, 8))
    password = ''.join(random.sample(string.ascii_letters, 8))
    payload = {
        "username": username,
        "password": password
    }
    r = requests.post(f'{config.API_URL}/users/', json=payload)
    assert r.status_code == 200


def test_post_token():
    global token
    payload = {"username": username, "password": password}
    r = requests.post(f'{config.API_URL}/token', data=payload)
    json = r.json()
    token = json['access_token']
    assert r.status_code == 200
