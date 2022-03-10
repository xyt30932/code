import requests, unittest
from laihua_web_api.download.pc_laihua_pfoo import Pfoo
from laihua_web_api.download.pc_laihua_video import Video
from laihua_web_api.download.updata_log import Updata_log

from utils import common_assert

s = requests.session()
host = "https://www.laihua.com"

class Test_member(unittest.TestCase):

    def setUp(self) -> None:
        self.s = requests.session()
        self.video = Video(s, host, "test003", "123456")
        self.pfoo = Pfoo(s, host, "test003", "123456")
        self.log = Updata_log(s, host, "test003", "123456")

    def tearDown(self) -> None:
        if self.s:
            self.s.close()

    # 来画视频
    def test_video_download(self):
        response = self.video.get_the_address()
        common_assert(self, response, 200, 200, "utm")

    # 来画演示
    def test_pfoo_download(self):
        response = self.pfoo.get_pfoo()
        common_assert(self, response, 200, 200, "perfooUpdatePC")

    # 获取更新日志
    def test_Updata_log(self):
        response = self.log.updata_log()
        common_assert(self, response, 200, 200, "title")


if __name__ == '__main__':
    unittest.main()