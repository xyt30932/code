
import requests
class RunMain():
    def send_get(self, url, data):
        response = requests.get(url, data)
        return response

    def send_post(self, url, data):
        response = requests.post(url, data)
        return response

    def run_main(self, method, url, data):

        if method == "get":
            response = self.send_get(url, data)

        else:
            response = self.send_post(url, data)

        return response
