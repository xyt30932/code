import requests, unittest
from laihua_web_api.member.demo_member import Demo
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert


class Test_demo_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.member = Demo(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 首次连续包月 特惠2折 9.9
    def test_First_continuous_monthly_payment(self):
        response = self.member.First_continuous_monthly_payment()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买一个月会员 特惠6折 39
    def test_month_membership(self):
        response = self.member.month_membership()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买三个月会员 特惠5折 68
    def test_Three_months_after_purchase(self):
        response = self.member.Three_months_after_purchase()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买十二个月会员 特惠4折 198
    def test_Buy_12_month_membership(self):
        response = self.member.Buy_12_month_membership()
        common_assert(self, response, 200, 200, "qrCode")

if __name__ == '__main__':
    unittest.main()