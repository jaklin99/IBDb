import os
import httpx

USERS_SERVICE_HOST_URL = 'http://localhost:8001/users'


def is_user_present(user_id: int):
    url = os.environ.get('USERS_SERVICE_HOST_URL') or USERS_SERVICE_HOST_URL
    r = httpx.get(f'{url}{user_id}')
    return True if r.status_code == 200 else False
