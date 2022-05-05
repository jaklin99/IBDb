import os
import httpx

USER_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/users/'

def is_user_present(cast_id: int):
    url = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False