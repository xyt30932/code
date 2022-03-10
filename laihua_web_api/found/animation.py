from api.login import Login

# 来画动画模板
class Animation():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)

    # 全部模板
    def all_template(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":""
        }
        return self.s.get(url, params=params)

    # 知识科普
    def Knowledge_of_popular_science(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141188"
        }
        return self.s.get(url, params=params)

        # 教育培训
    def Education_and_training(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141190"
        }
        return self.s.get(url, params=params)

    # 企业宣传
    def Enterprise_publicity(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141189"
        }
        return self.s.get(url, params=params)

    # 健康医疗
    def Health_care(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141191"
        }
        return self.s.get(url, params=params)

    # 金融科技
    def Financial_technology(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141371"
        }
        return self.s.get(url, params=params)

    # 抖音创意
    def Tiktok_Creativity(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141192"
        }
        return self.s.get(url, params=params)

    # 党建政务
    def The_party_affairs(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141193"
        }
        return self.s.get(url, params=params)

    # 抗击疫情
    def outbreak(self):
        url = self.host + "/webapi/common/findVideo"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"141623"
        }
        return self.s.get(url, params=params)


    # 我的收藏
    def collection(self):
        url = self.host + "/webapi/user/favorites/type"
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"my"
        }
        return self.s.get(url, params=params)

    # 搜素
    def search(self):
        url = self.host + "/webapi/common/findVideo"
        # keyword : 搜素
        params = {
            "type":"1",
            "findType":"1",
            "recommendPlatform":"1",
            "pIndex":"1",
            "fPage":"20",
            "sOfPage":"20",
            "category":"",
            "keyword":""
        }
        return self.s.get(url, params=params)


if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Animation(s, host,"test003", "123456")
    print(M.Financial_technology().json())
