import requests, unittest
from laihua_web_api.member.video_member import Video
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.member = Video(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 首次连续包月 特惠3折 19
    def test_First_continuous_monthly_payment(self):
        response = self.member.First_continuous_monthly_payment()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买一个月会员 特惠6折 40
    def test_month_membership(self):
        response = self.member.month_membership()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买三个月会员 特惠5折 88
    def test_Three_months_after_purchase(self):
        response = self.member.Three_months_after_purchase()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买十二个月会员 特惠4折 238
    def test_Buy_12_month_membership(self):
        response = self.member.Buy_12_month_membership()
        common_assert(self, response, 200, 200, "qrCode")

if __name__ == '__main__':
    unittest.main()