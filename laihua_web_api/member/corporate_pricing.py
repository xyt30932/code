
# 企业会员
from api.login import Login
class Pricing():
    def __init__(self,s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)

    # 获取会员商品列表、根据id获取会员信息
    def pricing(self):
        url = self.host + "/webapi/user/vipLevelInfo"
        r = self.s.get(url)
        return r

    # 企业荣耀版，4998/年，生成h5支付订单
    def Corporate_Honor_member(self):
        # goodsid ：会员id
        # month ：月数
        # nunber：子账号数量
        # automatic ：是否自动续费
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"67","month":"12"}
        r1 = self.s.post(url, json=body)
        return r1

    # 企业至尊版，9998/年，生成h5支付订单
    def Corporate_Supreme_Member(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"71","month":"12"}
        r2 = self.s.post(url, json=body)
        return r2

    # 企业旗舰套餐，19998/年，生成h5支付订单
    def Enterprise_flagship_package(self):
        url = self.host + "/webapi/user/vip/orders/createH5Order"
        body = {"goodsId":"75","month":"12"}
        r3 = self.s.post(url, json=body)
        return r3

    # 优惠券
    def coupons(self):
        url = self.host + "/webapi/user/coupon?type=1&pIndex=1&sOfPage=999&fPage=999&goodsType=1,2,3,4,5"
        r3 = self.s.get(url)
        return r3

if __name__ == '__main__':
    import requests
    s = requests.session()
    host = "https://www.laihua.com"
    M = Pricing(s, host, "xieyingtao", "xieyingtao")

