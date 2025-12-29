import pytest

from helpers.api_client import ApiClient
from helpers.user_helper import delete_user
from data.user_data import generate_user


client = ApiClient()


@pytest.fixture
def user_data():
    return generate_user()


@pytest.fixture
def registered_user(user_data):
    response = client.post("/auth/register", user_data)
    token = response.json().get("accessToken")
    yield {
        "user": user_data,
        "response": response,
        "token": token,
    }
    if token:
        delete_user(token)


@pytest.fixture
def authorized_headers(registered_user):
    return {
        "Authorization": registered_user["token"]
    }

@pytest.fixture
def cleanup_user():
    tokens = []
    yield tokens

    for token in tokens:
        delete_user(token)