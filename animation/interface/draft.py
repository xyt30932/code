from api.login import Login

class Interface():
    def __init__(self, s, host, account, psw):
        self.s = s
        self.host = host
        L = Login(s, host)
        L.login(account, psw)

    # 导入ppt
    def import_ppt(self):
        url = self.host + "/webapi/upload/ppt"
        files = {
        "files[]":("666.pptx", open("D://PPT//test5.pptx","rb"),
                   "application/vnd.openxmlformats-officedocument.presentationml.presentation")
        }
        r = self.s.post(url, files=files).json()
        filename = r["data"]["filename"]
        # print(filename)
        return r, filename

    def export_ppt(self, filename, title):
        url = self.host + "/webapi/user/draft/ppt"
        # "title":"test5.pptx",ppt标题
        body = {"filename":filename, "title":title}
        r1 = self.s.post(url, json=body).json()
        id = r1["data"]["projectId"]
        # print(id)
        return r1, id

    def export_id(self, id):
        url = self.host + "/webapi/user/draft"
        body = {"id":id}
        r2 = self.s.get(url, json=body).json()
        # print(type(r2))
        id_1 = r2["data"][0]["id"]
        # draftId
        ppt_id = r2["data"][1]["ppt"]
        project_id = r2["data"][2]["projectId"]

        # print(id_1, ppt_id, project_id)
        return r2, id_1, ppt_id, project_id

    def template_ppt(self,draftId):
        url = self.host + "/api/common/material"
        # "title":"test5.pptx",ppt标题
        body = {
            "type":"3",
            "pIndex":"1",
            "sOfPage": "24",
            "fPage": "24",
            "style": "78",
            "draftId": draftId,
            "dynamic": "3",
            "direction": "1",
            "allData":"1"
        }
        r3 = self.s.get(url, json=body).json()
        # 模板id resourceid scensid thumbnailUrl uuid draftid
        id = r3["data"][3]["id"]
        title = r3["data"][3]["title"]
        url = r3["data"][3]["url"]
        thumbnailUrl = r3["data"][3]["thumbnailUrl"]
        # print(id, thumbnailUrl, title, url)
        # 热带海滩岛棕榈树海洋暑假模板id
        return r3, id, url, thumbnailUrl, title

    def add_template(self, id):
        url = self.host + "/api/user/materialUseInfo"
        body = {"type":3,"id":id}
        r4 = self.s.post(url, json=body).json()
        return r4

    def add_template_1(self, id, resourceId, thumbnailUrl, draftId):
        url = self.host + "/api/user/material/checkCommercial"
        # id resourceid scensid thumbnailUrl uuid draftid\
        # dataList=[{"type":"bg","id":"72770f20-331b-11ec-a30e-acde48001122","resourceId":"72770f20-331b-11ec-a30e-acde48001122","fileType":1,"scenesId":"9a83cd3d_7c97_46ab_947b_fea16a2dc641","thumbnailUrl":"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png","uuid":"BG-9a83cd3d_7c97_46ab_947b_fea16a2dc641"}]
        body ={
            "dataList":[{"type":"bg","id":id,"resourceId":resourceId,"fileType":1,"scenesId":"9a83cd3d_7c97_46ab_947b_fea16a2dc641","thumbnailUrl":thumbnailUrl,"uuid":"BG-9a83cd3d_7c97_46ab_947b_fea16a2dc641"}],
            "draftId":draftId
        }
        r5 = self.s.post(url, json=body)
        return r5

    def draft(self, title, projectId):
        url = self.host + "/api/user/draft"
        body = {"title":title,"data":"{\"id\":\"635f7ab4_c1f3_4de9_9097_c55f89b24978\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"animations\":{\"duration\":0,\"delay\":0},\"easing\":\"linear\",\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[],\"musicLoop\":false},\"subtitle\":{}}","otherInfos":"{\"audios\":[]}","caption":"{}","times":10,"direction":1,"isPass":"","projectId":projectId,"templateId":"","removeMaterial":""}
        r6 = self.s.post(url, json=body).json()
        return r6

    def voice(self):
        url = self.host + "/api/user/audioAI/source"
        params = {}
        r7 = self.s.get(url, params=params).json()
        sourcename = r7["data"][0]["sourceId"]
        # print(sourcename)  #获取ai的sour配音

        return r7, sourcename

    def add_voice(self, text, speaker):
        url = self.host + "/api/user/audioAI"
        body = {"type":1,"text":text,"speaker":speaker,"speed":"5","provider":0,"pause_points":[],"isNotModified":"false"}
        r8 = self.s.post(url, json=body).json()
        sourceurl = r8["data"]["audioInfo"]["sourceUrl"]
        # print(sourceurl)
        return r8, sourceurl

    def user_voice(self, url_1,title):
        url = self.host + "/api/user/music"
        body = {"url":url_1,"title":title,"duration":1.2,"musicType":2,"fileType":50}
        r9 = self.s.post(url, json=body).json()
        return r9

    def draft_1(self, title,projectId):
        url = self.host + "/api/user/draft"
        body = {"title":title,"data":"{\"id\":\"51a6d553_6319_4dd9_bd75_fead9ae9a4f4\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"easing\":\"linear\",\"animations\":{\"duration\":0,\"delay\":0},\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[{\"title\":\"好的-来画小媛\",\"type\":1,\"fileType\":50,\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\",\"timeSlot\":[0,1.2],\"cut\":[0,1.2]}],\"musicLoop\":false},\"subtitle\":{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[]}}","otherInfos":"{\"audios\":[{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/53b24ca0-8ca1-11ec-9db7-2ff5d521bc87.mp3\"},{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/cb807720-8ca1-11ec-9db7-2ff5d521bc87.mp3\"},{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\"}]}","caption":"{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[]}","times":10,"direction":1,"isPass":"","projectId":projectId,"templateId":"","removeMaterial":""}
        r10 = self.s.post(url, json=body).json()
        return r10

    def video(self, title,projectId):
        url = self.host + "/api/user/video"
        body = {"projectId":projectId,"times":10,"title":title,"tags":"","description":"做短视频像做PPT一样简单？快挪步到“来画动画”一探究竟吧！","thumbnailUrl":"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png,2022-2-13/2fd14140-8ca8-11ec-9dc5-2f5594a3f97f.png,2022-2-13/2fd31600-8ca8-11ec-9db7-2ff5d521bc87.png","screen":"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png","data":"{\"id\":\"e2c3e6c9_a190_4693_9bf3_2ebe3003d82f\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"easing\":\"linear\",\"animations\":{\"duration\":0,\"delay\":0},\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[{\"title\":\"好的-来画小媛\",\"type\":1,\"fileType\":50,\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\",\"timeSlot\":[0,1.2],\"cut\":[0,1.2]}],\"musicLoop\":false},\"cover\":\"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png\",\"subtitle\":{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[{\"startTime\":0,\"endTime\":1.2,\"text\":\"好的\",\"outward\":{\"opacity\":1,\"rotation\":0,\"width\":1536,\"height\":0,\"x\":192,\"y\":972,\"isFlipped\":false},\"dropShadow\":{\"x\":0,\"y\":0,\"blur\":0,\"spread\":0,\"color\":\"#273F9F\"},\"font\":{\"color\":\"#303233\",\"fontSize\":54,\"fontFamilyUrl\":\"2018-5-16/1526467728442.TTF\",\"fontFamilyLabel\":\"方正黑体\",\"fontStretch\":\"normal\",\"fontWeight\":\"normal\",\"fontStyle\":\"normal\",\"textDecoration\":\"none\",\"textAlign\":\"center\",\"wordBreak\":\"break-word\",\"writingMode\":\"inherit\",\"myTextStroke\":1,\"myTextStrokeColor\":\"#ffffff\"}}]}}","watermark":"default","resolution":"480","music":"","optimized":"Horizontal","direction":0,"shareToSquare":1,"company":"","phone":"","isPersonalMaterial":"false","isLensFunction":"false","isWordCloud":"false","isBackgroundMusic":"false","isAutodraw":"false","isAIDubbing":"false","isInsertCoverToMp4":"true","backgroundMusicNumber":0,"isSubtitles":"true","haveInCommerical":0}
        r11 = self.s.post(url, json=body).json()
        return r11


if __name__ == '__main__':
    import requests, urllib3, logging
    logging.captureWarnings(True)
    urllib3.disable_warnings()
    s = requests.session()
    host = "https://www.laihua.com"
    M = Interface(s, host, "test003", "123456")
    r = M.import_ppt()
    print(r)
    r1 = M.export_ppt(str(r[1]), "enen")
    print(r1)
    r2 = M.export_id(str(r1[1]))
    print(r2)
    r3 = M.template_ppt(r2[1])
    print(r3)
    r4 = M.add_template(r3[1])
    print(r4)
    r5 = M.add_template_1(r3[1], r3[1], r3[3], r2[1])
    print(r5.text)
    r6 = M.draft("取名字真难", r2[1])
    print(r6)
    r7 = M.voice()
    print(r7)
    r8 = M.add_voice("好嘛", r7[1])
    print(r8)
    r9 = M.user_voice(r8[1],"知道了")
    print(r9)
    r10 = M.draft_1(r2[1],"enen")
    print(r10)
    r11 = M.video("xyt", r2[1])
    print(r11)