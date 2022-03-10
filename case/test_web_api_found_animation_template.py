import requests, unittest
from laihua_web_api.found.animation import Animation
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert01

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.found = Animation(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 全部模板
    def test_all_template(self):
        response = self.found.all_template()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)
        # self.assertTrue(r1 == response.json()["data"][1]["id"])

    # 知识科普
    def test_Knowledge_of_popular_science(self):
        response = self.found.Knowledge_of_popular_science()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 教育培训
    def test_Education_and_training(self):
        response = self.found.Education_and_training()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 企业宣传
    def test_Micro_class_make(self):
        response = self.found.Enterprise_publicity()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 健康医疗
    def test_Health_care(self):
        response = self.found.Health_care()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 金融科技
    def test_Financial_technology(self):
        response = self.found.Financial_technology()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 抖音创意
    def test_Tiktok_Creativity(self):
        response = self.found.Tiktok_Creativity()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 党建政务
    def test_The_party_affairs(self):
        response = self.found.The_party_affairs()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 抗击疫情
    def test_outbreak(self):
        response = self.found.outbreak()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)


if __name__ == '__main__':
    unittest.main()