from api.login import Login
# 来画视频
class Video():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)
        self.get_token = host + "/webapi/session/getToken"
        self.video = host + "/webapi/channel?utm=default&platform=12"

    def token(self):
        return  self.s.post(self.get_token)

    # 下载地址
    def get_the_address(self):
        return  self.s.get(self.video)

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Video(s, host, "test003", "123456")
    r1 = M.get_the_address()
    print(r1.json())

