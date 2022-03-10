
# 来画设计会员
from api.login import Login
class Design():
    def __init__(self,s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)

    # 首次连续包月 特惠2折
    def First_continuous_monthly_payment(self):
        # goodsid ：会员id
        # month ：月数
        # nunber：子账号数量
        # automatic ：是否自动续费
        # originalPrice ：原价
        # price ：实际价格
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"93","month":"1","automatic":"1"}
        r1 = self.s.post(url, json=body)
        return r1

    # 购买一个月会员 特惠6折
    def Purchase_for_one_month(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"93","month":"1","automatic":"1"}
        r2 = self.s.post(url, json=body)
        return r2

    # 购买三个月会员 特惠6折
    def Three_months_after_purchase(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"94","month":"3","automatic":"1"}
        r3 = self.s.post(url, json=body)
        return r3

    # 购买十二个月会员 特惠6折
    def Buy_12_month_membership(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"95","month":"12"}
        r4 = self.s.post(url, json=body)
        return r4


if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Design(s, host, "xieyingtao", "xieyingtao")

