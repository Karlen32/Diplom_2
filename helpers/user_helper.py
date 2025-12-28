from helpers.api_client import ApiClient

client = ApiClient()


def register_user(user_data):
    return client.post("/auth/register", user_data)


def login_user(credentials):
    return client.post("/auth/login", credentials)


def delete_user(access_token):
    headers = {"Authorization": access_token}
    return client.delete("/auth/user", headers=headers)