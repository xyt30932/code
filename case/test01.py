import unittest
from Base_requests import RunMain
class TestRun(unittest.TestCase):
    def setUp(self):
        self.run_main1 = RunMain()
    def test_01(self):
        url = 'https://www.laihua.com/webapi/login'
        data = {
            "account": "test003",
            "psw": "123456",
        }
        res = self.run_main1.run_main('post', url, data)
        print(res.json())
        self.assertEqual(200, res.status_code)

if __name__ == '__main__':
    unittest.main()