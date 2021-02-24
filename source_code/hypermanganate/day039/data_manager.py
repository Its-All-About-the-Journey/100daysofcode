from requests import Session, HTTPError


class DataManager:
    def __init__(
        self,
        endpoint: str,
        token: str,
         ) -> None:

        self.session = Session()
        self.endpoint = endpoint
        self.token = token

    def add(self,
            city: str,
            iata_code: str,
            lowest_price: int,
            ):

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        payload = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }

        results = self.session.post(
            self.endpoint,
            headers=headers,
            json=payload
            )

        try:

            results.raise_for_status()

        except HTTPError:

            print("Failed to insert to Google Sheet")
            return False

        else:

            return results.json()

    def read(self):

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        results = self.session.get(
            url=self.endpoint,
            headers=headers
        )

        try:

            results.raise_for_status()

        except HTTPError:

            print("Failed to read Google Sheet")
            return False

        else:

            sheet_data = results.json()['prices']
            return sheet_data

    def update(
        self, record_id: int, **kwargs
            ):

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        payload = {
            "price": {

            }
        }

        if "city" in kwargs:
            payload['price']['city'] = kwargs["city"],

        if "iataCode" in kwargs:
            payload['price']['iataCode'] = kwargs['iataCode']

        if "lowestPrice" in kwargs:
            payload['price']['lowestPrice'] = kwargs['lowestPrice']

        if len(payload['price']) == 0:
            print("No values submitted for update.")
            return False

        results = self.session.put(
            f"{self.endpoint}/{record_id}",
            headers=headers,
            json=payload
            )

        try:

            results.raise_for_status()

        except HTTPError:

            print("Failed to update Google Sheet")
            return False

        else:

            return results.json()
