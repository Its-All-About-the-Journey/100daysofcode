# 100 Days of Code: Python
# Pixela and Headers/HTTP Verbs
# Adam Pawlowski (@hypermanganate)

import requests
import datetime

from requests.models import HTTPError

USERID = "<userid>"
TOKEN = "<token>"


class Pixel:
    def __init__(
        self,
        quantity: int,
        graphid: str,
        username: str,
        token: str
         ) -> None:

        self.graphid = graphid
        self.username = username
        self.token = token
        self.quantity = quantity
        self.date = datetime.datetime.today().strftime("%Y%m%d")
        if not self.post_pixel():
            raise HTTPError

    def post_pixel(self):

        pixela_post_pixel_endpoint = \
            f"https://pixe.la/v1/users/{self.username}/graphs/{self.graphid}"

        pixela_post_pixel_json = {
            "date": self.date,
            "quantity": self.quantity,
        }

        pixela_headers = {
            "X-USER-TOKEN": token
        }

        response = requests.post(
            url=pixela_post_pixel_endpoint,
            json=pixela_post_pixel_json,
            headers=pixela_headers
        )

        if not response.status_code == 200 or \
           response.json()["isSuccess"] != "true":
            return False
        else:
            return True

    def update(self, quantity: int):

        pixela_update_pixel_endpoint = \
            f"https://pixe.la/v1/users/{self.username}/" + \
            f"graphs/{self.graphid}/{self.date}"

        pixela_update_pixel_json = {
            "quantity": quantity,
        }

        pixela_headers = {
            "X-USER-TOKEN": token
        }

        response = requests.put(
            url=pixela_update_pixel_endpoint,
            json=pixela_update_pixel_json,
            headers=pixela_headers
        )

        if not response.status_code == 200 or \
           response.json()["isSuccess"] != "true":
            return False
        else:
            return True

    def delete(self):

        pixela_update_pixel_endpoint = \
            f"https://pixe.la/v1/users/{self.username}/" + \
            f"graphs/{self.graphid}/{self.date}"

        pixela_headers = {
            "X-USER-TOKEN": token
        }

        response = requests.delete(
            url=pixela_update_pixel_endpoint,
            headers=pixela_headers
        )

        if not response.status_code == 200 or \
           response.json()["isSuccess"] != "true":
            return False
        else:
            return True


def create_user(desired_username: str, desired_token: str):

    pixela_new_user_endpoint = "https://pixe.la/v1/users"
    pixela_new_user_json = {
        "token": desired_token,
        "username": desired_username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(
        url=pixela_new_user_endpoint,
        json=pixela_new_user_json
        )

    if not response.status_code == 200 or \
       response.json()["isSuccess"] != "true":
        return False
    else:
        return True


def delete_user(username: str, token: str):

    pixela_delete_user_endpoint = f"https://pixe.la/v1/users/{username}"

    pixela_headers = {
        "X-USER-TOKEN": token
    }

    response = requests.delete(
        url=pixela_delete_user_endpoint,
        headers=pixela_headers
        )

    if not response.status_code == 200 or \
       response.json()["isSuccess"] != "true":
        return False
    else:
        return True


def create_integer_graph(
    username: str,
    token: str,
    id: str,
    name: str,
    unit: str
     ):
    # I did not add color as an option as this is just musing not a product

    pixela_new_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
    pixela_new_graph_json = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": "int",  # Or float
        "color": "momiji",
        }

    token_header = {
        "X-USER-TOKEN": token
    }

    response = requests.post(
        url=pixela_new_graph_endpoint,
        json=pixela_new_graph_json,
        headers=token_header
        )

    if not response.status_code == 200 or \
       response.json()["isSuccess"] != "true":
        return False
    else:
        return True

# Example


username = "postulio"
token = "bingbong"

create_user(desired_username=username, desired_token=token)
create_integer_graph(
    username,
    token,
    id="asdf1",
    name="Asdf Graph",
    unit="Bubbles"
    )

todays_pixel = Pixel(50, "asdf1", username, token)
todays_pixel.update(75)
todays_pixel.delete()

delete_user(username, token)
