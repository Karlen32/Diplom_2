from helpers.api_client import ApiClient

client = ApiClient()


def get_ingredients_ids():
    response = client.get("/ingredients")
    return [item["_id"] for item in response.json()["data"]]

INVALID_INGREDIENTS = ["123"]