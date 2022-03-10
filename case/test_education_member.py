import requests, unittest
from laihua_web_api.member.education_member import Education
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.member =  Education(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 领取教育免费会员
    def test_Get_free_education_membership(self):
        response = self.member.Get_free_education_membership()
        common_assert(self, response, 200, 200, "id")

    # 购买来画动画会员
    # 一个月 特惠七折 68
    def test_First_consecutive_package_season(self):
        response = self.member.First_consecutive_package_season()
        common_assert(self, response, 200, 200, "qrCode")

    # 三个月 特惠五折 98
    def test_First_consecutive_package_years(self):
        response = self.member.First_consecutive_package_years()
        common_assert(self, response, 200, 200, "qrCode")

    # 演示会员
    # 一个月 五折 26
    def test_Demo_for_month(self):
        response = self.member.Demo_for_month()
        common_assert(self, response, 200, 200, "qrCode")

    # 三个月 特惠四折 62
    def test_Demo_for_three_months(self):
        response = self.member.Demo_for_three_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 十二 特惠三折 174
    def test_Demo_for_twelve_months(self):
        response = self.member.Demo_for_twelve_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 视频会员
    # 一个月 四折 30
    def test_Video_for_month(self):
        response = self.member.Video_for_month()
        common_assert(self, response, 200, 200, "qrCode")

    # 三个月 特惠四折 68
    def test_Video_for_three_months(self):
        response = self.member.Video_for_three_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 十二 特惠三折 178
    def test_Video_for_twelve_months(self):
        response = self.member.Video_for_twelve_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 设计会员
    # 一个月 四折 30
    def test_Design_for_month(self):
        response = self.member.Design_for_month()
        common_assert(self, response, 200, 200, "qrCode")

    # 三个月 特惠四折 68
    def test_Design_for_three_months(self):
        response = self.member.Design_for_three_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 十二 特惠三折 178
    def test_Design_for_twelve_months(self):
        response = self.member.Design_for_twelve_months()
        common_assert(self, response, 200, 200, "qrCode")

    # 购买权益包
    def test_Purchase_interest_package(self):
        response = self.member.Purchase_interest_package()
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("code"))

if __name__ == '__main__':
    unittest.main()