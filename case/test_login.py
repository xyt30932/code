
from api.login import Login
from parameterized import parameterized
import requests,unittest,json,app,logging
from utils import common_assert01
s = requests.session()
host = "https://www.laihua.com"


def bulid_data():
    file = app.BASE_DIR + "/data/login.json"
    test_data = []
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)

        for case_data in json_data:
            account = case_data.get("account")
            psw = case_data.get("psw")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((account, psw, status_code,status,msg))
    return test_data

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = Login(s, host)
        self.s = s

    def tearDown(self):
        if self.s:
            self.s.close()

    @parameterized.expand(bulid_data())

    def test01_psw_error(self, account, psw, status_code, status, msg):
        response = self.login_api.login(account, psw)
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))

    def test02_success(self):
        response = self.login_api.login("test003", 123456)
        common_assert01(self, response, 200, 200)
