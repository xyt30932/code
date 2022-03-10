import requests, unittest
from laihua_web_api.member.corporate_pricing import Pricing
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.member = Pricing(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 获取会员商品列表、根据id获取会员信息
    def test_pricing(self):
        response = self.member.pricing()
        common_assert(self, response, 200, 200, "企业公益版会员")

    # 企业荣耀版，4998/年，生成h5支付订单
    def test_Corporate_Honor_member(self):
        response = self.member.Corporate_Honor_member()
        common_assert(self, response, 200, 200, "qrCode")

    # 企业至尊版，9998/年，生成h5支付订单
    def test_Corporate_Supreme_Member(self):
        response = self.member.Corporate_Supreme_Member()
        common_assert(self, response, 200, 200, "qrCode")

    # 企业旗舰套餐，19998/年，生成h5支付订单
    def test_Enterprise_flagship_package(self):
        response = self.member.Enterprise_flagship_package()
        common_assert(self, response, 200, 200, "qrCode")

    # 优惠券
    def test_coupons(self):
        response = self.member.coupons()
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("code"))

if __name__ == '__main__':
    unittest.main()