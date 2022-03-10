# 编辑器模板
import requests
s = requests.session()
host = "https://www.laihua.com"
from api.login import Login

class Template():

    def __init__(self, s, host):
        self.s = s
        self.host = host
        Login(s, host).login("test003", "123456")

    def import_ppt(self):
        files = {
        "files[]":("test5.pptx", open("D://PPT//test5.pptx","rb"),
                   "application/vnd.openxmlformats-officedocument.presentationml.presentation")
        }
        return self.s.post(url= host + "/webapi/upload/ppt", files=files)

    def export_ppt(self, filename,title):
        body = {"filename":filename, "title":title}
        return  self.s.post(url=host + "/webapi/user/draft/ppt",json=body)

    def export_id(self, id):
        body = {"id":id}
        return  self.s.get(url=host + "/webapi/user/draft",json=body)

    # 横板模板
    def get_template(self, draftId):
        url = self.host + "/api/home/template?/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword="
        body = {
            "draftId": draftId,
            "category":""
        }
        return  self.s.get(url=url, json=body)

    # 竖板模板
    def get_template_1(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=2&orderBy=11&payType=&isCommerical=&keyword=&"
        # direction 判断横竖版
        body = {
            "draftId": draftId,
            "category":""
        }
        return self.s.get(url, json=body)

    # 企业宣传
    def Enterprise_publicity(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142312"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 科普讲解
    def Popular_science_explain(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142313"
        body = {
            "draftId": draftId
        }
        return self.s.get(url, json=body)

    # 教育培训
    def Education_and_training(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142314"
        body = {
            "draftId": draftId
        }
        return self.s.get(url, json=body)

    # 健康医疗
    def Health_care(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142315"
        body = {
            "draftId": draftId,
            "category": "142315"
        }
        return self.s.get(url, json=body)

    # 金融财经
    def Financial_financial(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142316"
        body = {
            "draftId": draftId
        }
        return self.s.get(url, json=body)

    # 行政管理
    def The_administrative_management(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142317"
        body = {
            "draftId": draftId
        }
        return self.s.get(url, json=body)

    # 党建政务
    def The_party_affairs(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142318"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 快闪动画
    def Fast_flashing_paint(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142319"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 广告营销
    def Advertising_and_marketing(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142320"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 节日热点
    def Holiday_hot_spots(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142321"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 互联网
    def Internet(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142322"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 传播媒体
    def media(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142323"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 电子相册
    def Electronic_photo_album(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142324"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 电商
    def electricity(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142325"
        body = {
            "draftId": draftId,
            "category": "142325"
        }
        return self.s.get(url, json=body)

    # 产品介绍
    def Product_introduction(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142419"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 视频简历
    def Video_resume(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=142500"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 2月新增
    def In_February_the_new(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=&isCommerical=&keyword=&category=143640"
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)


    # 横板全部分类 免费
    def free(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=0&isCommerical=&keyword=&category="
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)


    # 横板全部分类 会员专属
    def membership(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&direction=1&orderBy=11&payType=1,4&isCommerical=&keyword=&category="
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

    # 横板全部分类 企业会员专属
    def Exclusive_to_corporate_members(self, draftId):
        url = self.host + "/api/home/template?pIndex=1&sOfPage=24&fPage=24&style=78&draftId=f6b49fe2-0561-48f3-bc14-f9b168ae9cb7&direction=1&orderBy=11&payType=6&isCommerical=&keyword=&category="
        body = {
            "draftId": draftId,
        }
        return self.s.get(url, json=body)

if __name__ == '__main__':
    M = Template(s, host)
    print(M.import_ppt().json())








