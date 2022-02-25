import requests, unittest
from api.import_ppt import Import_ppt
from api.login import Login

s = requests.session()
host = "https://www.laihua.com"
from utils import common_assert
from utils import common_assert01
class Test_Import_ppt(unittest.TestCase):

    def setUp(self):
        self.login  = Login(s, host).login("test003", 123456)
        self.s = s
        self.url = Import_ppt(s,host)
        self.host = Import_ppt(s,host)
        self.get_id = Import_ppt(s, host)
        self.template_id = Import_ppt(s, host)
        self.add = Import_ppt(s, host)
        self.get_draft = Import_ppt(s, host)
        self.draft  = Import_ppt(s, host)
        self.get_song = Import_ppt(s, host)
        self.user_voice = Import_ppt(s, host)
        self.api_draft = Import_ppt(s, host)
        self.video = Import_ppt(s, host)

    def tearDown(self):
        if self.s:
            self.s.close()

    def test_export_id(self):
        r = self.url.import_ppt().json()
        filename = r["data"]["filename"]
        r1 = self.host.export_ppt(filename,"enen").json()
        id = r1["data"]["projectId"]
        response = self.get_id.export_id(id)
        draftid = response.json()["data"][0]["id"]
        common_assert01(self, response, 200, 200)
        response = self.template_id.template_ppt(draftid)
        id_1 = response.json()["data"][3]["id"]
        thumbnailUrl = response.json()["data"][3]["thumbnailUrl"]
        common_assert01(self, response, 200, 200)
        add_template = self.add.add_template(id_1)
        self.assertEqual(200, add_template.status_code)
        response = self.get_draft.add_template_1(id_1, id_1,thumbnailUrl, draftid)
        common_assert01(self, response, 200, 200)
        response = self.draft.save("haoma", id)
        common_assert(self, response, 200, 200, "projectId")
        response = self.get_song.voice()
        sourcename = response.json()["data"][0]["sourceId"]
        common_assert01(self, response, 200, 200)
        response = self.user_voice.user("难受", sourcename)
        common_assert(self, response, 200, 200, "id")
        response = self.api_draft.draft_1("很难受", id)
        common_assert(self, response, 200, 200, "projectId")
        response = self.video.save_1("难受的一批", id)
        common_assert(self, response, 200, 200, "id")
