import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint_path):
        full_url = self.base_url + endpoint_path
        response = requests.get(full_url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
