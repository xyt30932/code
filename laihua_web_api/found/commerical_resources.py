from api.login import Login

# 正版商用资源
class Resources():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)

    # 背景
    def background(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"3",
            "fPage":"21",
            "sOfPage":"21",
            "isHome":"false"
        }
        return self.s.get(url, params=params)

    # 角色
    def role(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"14",
            "fPage":"42",
            "sOfPage":"42",
            "isHome":"false"
        }
        return self.s.get(url, params=params)

    # 素材
    def material(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"17",
            "fPage":"42",
            "sOfPage":"42",
            "isHome":"false"
        }
        return self.s.get(url, params=params)

    # 文字
    def text(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"16",
            "fPage":"42",
            "sOfPage":"42",
            "isHome":"false"
        }
        return self.s.get(url, params=params)

    # 音乐
    def music(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"5",
            "fPage":"32",
            "sOfPage":"32",
            "isHome":"false"
        }
        return self.s.get(url, params=params)

    # 正版角色
    def original_role(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"14",
            "fPage":"20",
            "isHome":"true"
        }
        return self.s.get(url, params=params)

    # 正版素材
    def original_material(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"17",
            "fPage":"20",
            "isHome":"true"
        }
        return self.s.get(url, params=params)

    # 正版文字
    def original_text(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"16",
            "fPage":"20",
            "isHome":"true"
        }
        return self.s.get(url, params=params)

    # 正版背景
    def original_background(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"3",
            "fPage":"100",
            "isHome":"true"
        }
        return self.s.get(url, params=params)


    # 正版音乐
    def original_music(self):
        url = self.host + "/webapi/common/material/getMaterialByTypeAndCategory"
        params = {
            "type":"5",
            "fPage":"20",
            "isHome":"true"
        }
        return self.s.get(url, params=params)

    # 首页banner
    def banner(self):
        url = self.host + "/webapi/home/banner?type=1&category=30"
        return self.s.get(url)


if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Resources(s, host,"test003", "123456")
    print(M.banner().json()["data"][0]["id"])
