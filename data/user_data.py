import uuid


def generate_user():
    return {
        "email": f"test_{uuid.uuid4()}@mail.ru",
        "password": "123456",
        "name": "Test User"
    }