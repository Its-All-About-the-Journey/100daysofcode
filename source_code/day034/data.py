import requests

URL = "https://opentdb.com/api.php"

PARAMS= {
    "amount": 10,
    "type": "boolean"
}


def db_request(url: str, params: dict) -> list:
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    return response.json()["results"]


question_data = db_request(URL, PARAMS)


if __name__ == "__main__":
    print(question_data)
