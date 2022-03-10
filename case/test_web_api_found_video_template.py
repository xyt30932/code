import requests, unittest
from laihua_web_api.found.video import Video
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert01

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.found = Video(s, host, "xieyingtao", "xieyingtao")

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

    # 科普讲解
    def test_Popular_science_explain(self):
        response = self.found.Popular_science_explain()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 行业干货
    def test_Dry_goods_industry(self):
        response = self.found.Dry_goods_industry()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 微课制作
    def test_Micro_class_make(self):
        response = self.found.Micro_class_make()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)
    # 自我介绍
    def test_introduce_myself(self):
        response = self.found.introduce_myself()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)
    # 产品介绍
    def test_Product_introduction(self):
        response = self.found.Product_introduction()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)
    # 微课制作
    def test_News_consulting(self):
        response = self.found.News_consulting()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)


if __name__ == '__main__':
    unittest.main()