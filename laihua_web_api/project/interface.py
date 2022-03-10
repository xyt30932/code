
# 创作主页   全部项目
from api.login import Login

class Project():
    def __init__(self,s, host, account, psw):
        self.s = s
        self.host = host
        Login(s,host).login(account, psw)

    # 动画项目,未完成草稿
    def cartoon_project(self):
        url = self.host + "/user/draft?keyword=&sOfPage=24&fPage=24&orderBy=2&getAll=1"
        return self.s.get(url)

    # 动画项目，已完成作品
    def cartoon_project_1(self):
        url = self.host + "/webapi/user/video?sOfPage=24&fPage=24&keyword=&pIndex=1&getAll=1"
        return self.s.get(url)

    # 动画项目，搜素
    def cartoon_search(self):
        url = self.host + "/webapi/user/draft?sOfPage=24&fPage=24&orderBy=2"
        body = {
            "keyword":"1"
        }
        return self.s.get(url, json=body)

    # 白板项目
    def whiteboard_project(self):
        url = self.host + "/webapi/user/baiban/project?pIndex=1&sOfPage=24&fPage=24&category=&platform=22"
        return self.s.get(url)

    # 白板项目，搜素
    def whiteboard_search(self):
        url = self.host + "/webapi/user/baiban/project?pIndex=1&sOfPage=24&fPage=24&category=&platform=22"
        body = {
            "keyword":"1"
        }
        return self.s.get(url, json=body)

    # 设计项目
    def laihuadesign_project(self):
        url = self.host + "/laihuadesign/user/draft?pIndex=1&keyword=&sOfPage=20&fPage=20"
        return self.s.get(url)

    # 设计项目，搜素
    def laihuadesign_search(self):
        url = self.host + "/laihuadesign/user/draft?pIndex=1&sOfPage=20&fPage=20"
        body = {
            "keyword":"1"
        }
        return self.s.get(url, json=body)

    # 演示项目
    def demo_project(self):
        url = self.host + "/webapi/user/cloudDoc?keyword=&sOfPage=24&fPage=24&orderBy=2&getAll=1"
        return self.s.get(url)

    # 演示项目，搜素
    def demo_search(self):
        url = self.host + "/webapi/user/cloudDoc?sOfPage=24&fPage=24&orderBy=2&getAll=1"
        body = {
            "keyword":"1"
        }
        return self.s.get(url, json=body)


if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Project(s, host, "test003", "123456")
    # print(M.demo_project().json())

