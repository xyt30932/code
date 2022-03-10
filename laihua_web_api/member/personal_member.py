
# 来画动画会员
from api.login import Login
class Personal():
    def __init__(self,s, host, account, psw):
        self.s = s
        self.host = host
        Login(s, host).login(account, psw)

    # 首次连续包月，78/月自动续费 特惠八折
    def First_continuous_monthly_payment(self):
        # goodsid ：会员id
        # month ：月数
        # nunber：子账号数量
        # automatic ：是否自动续费
        # originalPrice ：原价
        # price ：实际价格
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"55","month":"1","automatic":"1"}
        return  self.s.post(url, json=body)

    # 首次连续包季 118/月自动续费 特惠六折
    def First_consecutive_package_season(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"38","month":"3","automatic":"1"}
        return self.s.post(url, json=body)

    # 首次连续包年 349/月自动续费 特惠五折
    def First_consecutive_package_years(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"40","month":"12","automatic":"1"}
        return self.s.post(url, json=body)

    # 原价购买一个月
    def A_month(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"55","month":"1"}
        return self.s.post(url, json=body)

    # 特惠八折三个月
    def percent_off_for_three_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"38","month":"3"}
        return  self.s.post(url, json=body)

    # 特惠七折十二个月
    def off_for_12_months(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"40","month":"12"}
        return self.s.post(url, json=body)

    # 购买权益包
    def Purchase_interest_package(self):
        url = self.host + "/webapi/user/vip/rights?levelType=0"
        return self.s.get(url)

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Personal(s, host, "xieyingtao", "xieyingtao")

