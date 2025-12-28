import pytest
from helpers.api_client import ApiClient
from helpers.user_helper import delete_user
from data.user_data import generate_user

client = ApiClient()


@pytest.fixture
def authorized_user():
    user = generate_user()
    reg = client.post("/auth/register", user)
    token = reg.json()["accessToken"]
    headers = {"Authorization": token}

    yield headers

    delete_user(token)


@pytest.fixture
def registered_user():
    user = generate_user()
    reg = client.post("/auth/register", user)
    token = reg.json().get("accessToken")
    
    yield {"user": user, "token": token, "response": reg}
    
    if token:
        delete_user(token)