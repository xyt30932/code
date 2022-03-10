
import requests
s = requests.session()
host = "https://www.laihua.com"
from api.login import Login
class Import():
    def __init__(self, s, host):
        Login(s, host).login("test003", "123456")
        self.s = s
        self.host = host

    def import_ppt(self):
        files = {
            "files[]" :("test5.pptx", open("D://PPT//test5.pptx" ,"rb"),
                       "application/vnd.openxmlformats-officedocument.presentationml.presentation")
        }
        return self.s.post(url= host + "/webapi/upload/ppt", files=files)

    def export_ppt(self, filename):
        body = {"filename" :filename, "title" :"xyt"}
        return  self.s.post(url= host + "/webapi/user/draft/ppt", json=body)

    def export_id(self, id):
        body = {"id" :id}
        return  self.s.get(url= host + "/webapi/user/draft",json=body)

