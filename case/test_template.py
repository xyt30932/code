from animation.interface.template import Template
import requests, unittest
s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert
from utils import common_assert01
from api.login import Login

class Test_demo_member(unittest.TestCase):
    def setUp(self) -> None:
        self.s = requests.session()
        Login(s, host).login("test003", "123456")

        self.template = Template(s, host)

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    def test_template(self):
        r = self.template.import_ppt().json()
        filename = r["data"]["filename"]
        r1 = self.template.export_ppt(filename,"enen").json()
        id = r1["data"]["projectId"]
        response = self.template.export_id(id)
        draftId = response.json()["data"][0]["id"]
        common_assert01(self, response, 200,200)

        response = self.template.get_template(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.get_template_1(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Enterprise_publicity(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Popular_science_explain(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Education_and_training(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Health_care(draftId)
        common_assert01(self, response, 200, 200)


        response = self.template.Financial_financial(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.The_administrative_management(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.The_party_affairs(draftId)
        common_assert01(self, response, 200, 200)


        response = self.template.Fast_flashing_paint(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Advertising_and_marketing(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Holiday_hot_spots(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Internet(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.media(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Electronic_photo_album(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.electricity(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Product_introduction(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Video_resume(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.In_February_the_new(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.free(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.membership(draftId)
        common_assert01(self, response, 200, 200)

        response = self.template.Exclusive_to_corporate_members(draftId)
        common_assert01(self, response, 200, 200)

if __name__ == '__main__':
    unittest.main()