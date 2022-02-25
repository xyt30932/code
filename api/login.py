import requests
s = requests.session()
host = "https://www.laihua.com"

class Login():

    def __init__(self, s, host):
        self.url_login = host + "/webapi/login"
        self.s = s

    def login(self, account, psw):
        login_data = {"account":account, "psw":psw}
        return self.s.post(url=self.url_login, data=login_data)