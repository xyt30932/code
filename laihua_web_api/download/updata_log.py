

from api.login import Login
# 获取更新日志
class Updata_log():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)

    def updata_log(self):
        url = self.host + "/webapi/introduction/10"
        r = self.s.get(url)
        return r

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Updata_log(s, host,"test003", "123456").updata_log()
    print(M.text)