import requests, unittest
from laihua_web_api.member.personal_member import Personal
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.member = Personal(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 首次连续包月，78/月自动续费 特惠八折
    def test_First_continuous_monthly_payment(self):
        response = self.member.First_continuous_monthly_payment()
        common_assert(self, response, 200, 200, "qrCode")

    # 首次连续包季 118/月自动续费 特惠六折
    def test_First_consecutive_package_season(self):
        response = self.member.First_consecutive_package_season()
        common_assert(self, response, 200, 200, "qrCode")

    # 首次连续包年 349/月自动续费 特惠五折
    def test_First_consecutive_package_years(self):
        response = self.member.First_consecutive_package_years()
        common_assert(self, response, 200, 200, "qrCode")

    # 原价购买一个月
    def test_A_month(self):
        response = self.member.A_month()
        common_assert(self, response, 200, 200, "qrCode")

    # 特惠八折三个月
    def test_percent_off_for_three_months(self):
        response = self.member.percent_off_for_three_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 特惠七折十二个月
    def test_off_for_12_months(self):
        response = self.member.off_for_12_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 特惠八折三个月
    def test_Purchase_interest_package(self):
        response = self.member.percent_off_for_three_months()
        common_assert(self, response, 200, 200, "qrCode")

if __name__ == '__main__':
    unittest.main()