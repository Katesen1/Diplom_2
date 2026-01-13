import pytest
import requests
from extra import const

@pytest.fixture
def delete_user():
    tokens_to_delete = []
    yield tokens_to_delete
    for token in tokens_to_delete:
        requests.delete(const.BASE_URL + const.DELETE_USER_HANDLE,headers={'Authorization': token})
