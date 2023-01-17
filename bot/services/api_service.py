import requests as req


class ApiSevrvice:
    panel_base_url = 'http://148.251.119.110/:13833'

    def login(self):
        response = req.post(
            self.panel_base_url + 'login?username=admin&password=admin',
            headers={
                "accept": "application/json, text/plain, /",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            params={
                'username': 'admin',
                'password': 'admin'
            }
        )
        print(response.status_code)
        print(response.text)

    def fetch_inbounds(self):
        response = req.get(
        )
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            raise req.exceptions.ConnectionError()


api = ApiSevrvice()
print(api.login())
