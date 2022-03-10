from api.login import Login

# 来画视频模板
class Video():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)

    # 全部模板
    def all_template(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"",
            "pIndex":"",
            "fPage":"",
            "sOfPage":"",
            "category":""
        }
        return self.s.get(url, params=params)

    # 科普讲解
    def Popular_science_explain(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142746"
        }
        return self.s.get(url, params=params)

    # 行业干货
    def Dry_goods_industry(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142749"
        }
        return self.s.get(url, params=params)

    # 微课制作
    def Micro_class_make(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142745"
        }
        return self.s.get(url, params=params)

    # 自我介绍
    def introduce_myself(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142747"
        }
        return self.s.get(url, params=params)

    # 产品介绍
    def Product_introduction(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142748"
        }
        return self.s.get(url, params=params)

    # 新闻咨询
    def News_consulting(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "fileType":"49",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"142750"
        }
        return self.s.get(url, params=params)


if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Video(s, host,"test003", "123456")
