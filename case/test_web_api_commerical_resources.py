import requests, unittest
from laihua_web_api.found.commerical_resources import Resources
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert01

class Test_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        self.resources = Resources(s, host, "xieyingtao", "xieyingtao")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 背景
    def test_background(self):
        response = self.resources.background()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)
        self.assertTrue(r1 == response.json()["data"][1]["id"])

    # 角色
    def test_role(self):
        response = self.resources.role()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 素材
    def test_material(self):
        response = self.resources.material()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 文字
    def test_text(self):
        response = self.resources.text()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 音乐
    def test_music(self):
        response = self.resources.music()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 正版角色
    def test_original_role(self):
        response = self.resources.original_role()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 正版素材
    def test_original_material(self):
        response = self.resources.original_material()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 正版文字
    def test_original_text(self):
        response = self.resources.original_text()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 正版背景
    def test_original_background(self):
        response = self.resources.original_background()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 正版音乐
    def test_original_music(self):
        response = self.resources.original_music()
        r = response.json()
        r1 = (r["data"][1])["id"]
        self.assertIn(r1, response.json()["data"][1].get("id"))
        common_assert01(self, response, 200, 200)

    # 首页banner
    def test_banner(self):
        response = self.resources.banner()
        r = response.json()
        r1 = (r["data"][0])["id"]
        self.assertTrue(r1, response.json()["data"][0].get("id"))
        common_assert01(self, response, 200, 200)


if __name__ == '__main__':
    unittest.main()