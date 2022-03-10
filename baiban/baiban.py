from api.login import Login
# 来画白板
class Baiban():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)
        self.get_template = host + "/whimark-api/template?sOfPage=18&fPage=18&pIndex=1"

    def template(self):
        return self.s.get(self.get_template)

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://beta.laihua.com"
    print(Baiban(s, host, "test003", "123456").template().json())

