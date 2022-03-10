
# 教育会员
from api.login import Login
class Education():
    def __init__(self,s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)

    # 领取教育免费会员
    def Get_free_education_membership(self):
        # goodsid ：会员id
        # month ：月数
        # nunber：子账号数量
        # automatic ：是否自动续费
        # originalPrice ：原价
        # price ：实际价格
        url = self.host + "/webapi/user/info/applyInfo?type=23"
        r1 = self.s.get(url)
        return r1

    # 购买来画动画会员
    # 一个月 特惠七折 68
    def First_consecutive_package_season(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"55","month":"1"}
        r2 = self.s.post(url, json=body)
        return r2

    # 三个月 特惠五折 98
    def First_consecutive_package_years(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"38","month":"3"}
        r3 = self.s.post(url, json=body)
        return r3

    # 演示会员
    # 一个月 五折 26
    def Demo_for_month(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"76","month":"1"}
        r4 = self.s.post(url, json=body)
        return r4

    # 三个月 特惠四折 62
    def Demo_for_three_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"80","month":"3"}
        r5 = self.s.post(url, json=body)
        return r5

    # 十二 特惠三折 174
    def Demo_for_twelve_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"81","month":"12"}
        r6 = self.s.post(url, json=body)
        return r6

    # 视频会员
    # 一个月 四折 30
    def Video_for_month(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"49","month":"1"}
        r7 = self.s.post(url, json=body)
        return r7

    # 三个月 特惠四折 68
    def Video_for_three_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"50","month":"3"}
        r8 = self.s.post(url, json=body)
        return r8

    # 十二 特惠三折 178
    def Video_for_twelve_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"51","month":"12"}
        r9 = self.s.post(url, json=body)
        return r9

    # 设计会员
    # 一个月 四折 30
    def Design_for_month(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"93","month":"1"}
        r10 = self.s.post(url, json=body)
        return r10

    # 三个月 特惠四折 68
    def Design_for_three_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"94","month":"3"}
        r11 = self.s.post(url, json=body)
        return r11

    # 十二 特惠三折 178
    def Design_for_twelve_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"95","month":"12"}
        r12 = self.s.post(url, json=body)
        return r12

    # 购买权益包
    def Purchase_interest_package(self):
        url = self.host + "/webapi/user/vip/rights?levelType=0"
        r13 = self.s.get(url)
        return r13

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Education(s, host, "xieyingtao", "xieyingtao")
    print(M.Purchase_interest_package().text)