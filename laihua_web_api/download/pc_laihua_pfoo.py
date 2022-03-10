from api.login import Login

# 来画演示下载
class Pfoo():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)
        self.pfoo = host + "/webapi/common/config?type=120"

    def get_token(self):
        url = self.host + "/webapi/session/getToken"
        cookies = {
            "distinct_id": "17d2be61499b5d-06813aa50c4a728-978183a-1296000-17d2be6149aa9b",
        }

        r = self.s.post(url=url, cookies=cookies).json()
        token = r["data"]
        return r, token

    # 下载地址
    def get_pfoo(self):
        # url = self.host + "/webapi/common/config?type=120"
        # headers = {"token": r[1]}
        return  self.s.get(self.pfoo)
        # downloadUrl = r1["data"]["perfooUpdatePC"]
        # print(downloadUrl)
        # return r1


if __name__ == '__main__':
    import requests,re
    s = requests.session()
    host = "https://www.laihua.com"
    M = Pfoo(s, host,"test003", "123456")
    r = M.get_token()
    r1 = M.pfoo()
    print(r1)