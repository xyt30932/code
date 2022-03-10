
import requests
s = requests.session()
host = "https://www.laihua.com"

class Import_ppt():
    def __init__(self, s, host):
        self.url = host + "/webapi/upload/ppt"
        self.s = s
        self.host = host + "/webapi/user/draft/ppt"
        self.get_id = host + "/webapi/user/draft"
        self.template_id = host + "/api/common/material"
        self.add = host + "/api/user/materialUseInfo"
        self.get_draft = host + "/api/user/material/checkCommercial"
        self.draft = host + "/api/user/draft"
        self.get_song = host + "/api/user/audioAI/source"
        self.user_voice = host + "/api/user/music"
        self.api_draft = host + "/api/user/draft"
        self.video = host + "/api/user/video"

    def import_ppt(self):
        files = {
        "files[]":("test5.pptx", open("D://PPT//test5.pptx","rb"),
                   "application/vnd.openxmlformats-officedocument.presentationml.presentation")
        }
        return self.s.post(url=self.url, files=files)

    def export_ppt(self, filename,title):
        body = {"filename":filename, "title":title}
        return  self.s.post(url=self.host, json=body)

    def export_id(self, id):
        body = {"id":id}
        return  self.s.get(url=self.get_id,json=body)

    def template_ppt(self,draftId):
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
        return self.s.get(url=self.template_id, json=body)

    def add_template(self, id):
        body = {"type":3,"id":id}
        return self.s.post(url=self.add, json=body)

    def add_template_1(self, id, resourceId, thumbnailUrl, draftId):
        body ={
            "dataList":[{"type":"bg","id":id,"resourceId":resourceId,"fileType":1,"scenesId":"9a83cd3d_7c97_46ab_947b_fea16a2dc641","thumbnailUrl":thumbnailUrl,"uuid":"BG-9a83cd3d_7c97_46ab_947b_fea16a2dc641"}],
            "draftId":draftId
        }
        return self.s.post(url=self.get_draft, json=body)

    def save(self, title, projectId):
        body = {"title":title,"data":"{\"id\":\"635f7ab4_c1f3_4de9_9097_c55f89b24978\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"animations\":{\"duration\":0,\"delay\":0},\"easing\":\"linear\",\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[],\"musicLoop\":false},\"subtitle\":{}}","otherInfos":"{\"audios\":[]}","caption":"{}","times":10,"direction":1,"isPass":"","projectId":projectId,"templateId":"","removeMaterial":""}
        return self.s.post(url = self.draft, json=body)

    def voice(self):
        return  self.s.get(self.get_song)

    def user(self, url_1,title):
        body = {"url":url_1,"title":title,"duration":1.2,"musicType":2,"fileType":50}
        return  self.s.post(url=self.user_voice, json=body)

    def draft_1(self, title,projectId):
        body = {"title":title,"data":"{\"id\":\"51a6d553_6319_4dd9_bd75_fead9ae9a4f4\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"easing\":\"linear\",\"animations\":{\"duration\":0,\"delay\":0},\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[{\"title\":\"好的-来画小媛\",\"type\":1,\"fileType\":50,\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\",\"timeSlot\":[0,1.2],\"cut\":[0,1.2]}],\"musicLoop\":false},\"subtitle\":{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[]}}","otherInfos":"{\"audios\":[{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/53b24ca0-8ca1-11ec-9db7-2ff5d521bc87.mp3\"},{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/cb807720-8ca1-11ec-9db7-2ff5d521bc87.mp3\"},{\"pause_points\":[],\"provider\":0,\"speaker\":\"x2_xiaoyuan\",\"speed\":5,\"text\":\"好的\",\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\"}]}","caption":"{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[]}","times":10,"direction":1,"isPass":"","projectId":projectId,"templateId":"","removeMaterial":""}
        return  self.s.post(self.api_draft, json=body)

    def save_1(self, title,projectId):
        body = {"projectId":projectId,"times":10,"title":title,"tags":"","description":"做短视频像做PPT一样简单？快挪步到“来画动画”一探究竟吧！","thumbnailUrl":"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png,2022-2-13/2fd14140-8ca8-11ec-9dc5-2f5594a3f97f.png,2022-2-13/2fd31600-8ca8-11ec-9db7-2ff5d521bc87.png","screen":"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png","data":"{\"id\":\"e2c3e6c9_a190_4693_9bf3_2ebe3003d82f\",\"title\":\"my works\",\"sound\":null,\"scenes\":[{\"sceneId\":\"acede1d2-5748-4803-a714-813c347eea2d\",\"sprites\":[],\"index\":0,\"resourceId\":null,\"vipMaterials\":[],\"vipFunctions\":[],\"background\":{\"trackingType\":\"0000\",\"fileType\":1,\"resourceId\":\"72770f20-331b-11ec-a30e-acde48001122\",\"type\":\"Image\",\"url\":\"2021-10-22/72fbbde8-32de-11ec-bf6b-acde48001122.png\",\"color\":null,\"opacity\":1,\"blur\":0,\"startTime\":0,\"duration\":10,\"laying\":\"fill\",\"filter\":{\"blur\":0,\"brightness\":1,\"contrast\":1,\"saturate\":1,\"grayscale\":0,\"hueRotate\":0,\"invert\":0,\"sepia\":0},\"effect\":{\"zoomStartTime\":0,\"zoomEndTime\":0,\"zoomStartScale\":1,\"zoomEndScale\":1,\"type\":\"zoom\"}},\"sound\":null,\"duration\":10,\"enterEffect\":{\"type\":\"None\",\"duration\":1},\"exitEffect\":{\"type\":\"None\",\"duration\":1},\"groupList\":[],\"cameras\":[{\"matrix\":{\"w\":1920,\"h\":1080,\"x\":0,\"y\":0,\"r\":0},\"easing\":\"linear\",\"animations\":{\"duration\":0,\"delay\":0},\"scale\":1}],\"version\":\"4.0\"}],\"resolution\":{\"width\":1920,\"height\":1080},\"optimized\":\"Horizontal\",\"version\":\"5.4.0\",\"productionPlatform\":\"Web\",\"watermarkInfo\":null,\"targetPlatform\":\"UWP\",\"music\":{\"volume\":[50,50,100],\"data\":[{\"title\":\"好的-来画小媛\",\"type\":1,\"fileType\":50,\"url\":\"2022-2-13/8aa54400-8ca2-11ec-9dc5-2f5594a3f97f.mp3\",\"timeSlot\":[0,1.2],\"cut\":[0,1.2]}],\"musicLoop\":false},\"cover\":\"2022-2-13/2fcdbed0-8ca8-11ec-9db7-2ff5d521bc87.png\",\"subtitle\":{\"id\":\"35d1f527-6794-4ae6-9bac-5bb82248c099\",\"title\":\"爱拼才会赢\",\"url\":\"\",\"type\":\"draft\",\"productionPlatform\":\"web\",\"duration\":10,\"optimized\":\"Horizontal\",\"resolution\":{\"height\":1080,\"width\":1920},\"contents\":[{\"startTime\":0,\"endTime\":1.2,\"text\":\"好的\",\"outward\":{\"opacity\":1,\"rotation\":0,\"width\":1536,\"height\":0,\"x\":192,\"y\":972,\"isFlipped\":false},\"dropShadow\":{\"x\":0,\"y\":0,\"blur\":0,\"spread\":0,\"color\":\"#273F9F\"},\"font\":{\"color\":\"#303233\",\"fontSize\":54,\"fontFamilyUrl\":\"2018-5-16/1526467728442.TTF\",\"fontFamilyLabel\":\"方正黑体\",\"fontStretch\":\"normal\",\"fontWeight\":\"normal\",\"fontStyle\":\"normal\",\"textDecoration\":\"none\",\"textAlign\":\"center\",\"wordBreak\":\"break-word\",\"writingMode\":\"inherit\",\"myTextStroke\":1,\"myTextStrokeColor\":\"#ffffff\"}}]}}","watermark":"default","resolution":"480","music":"","optimized":"Horizontal","direction":0,"shareToSquare":1,"company":"","phone":"","isPersonalMaterial":"false","isLensFunction":"false","isWordCloud":"false","isBackgroundMusic":"false","isAutodraw":"false","isAIDubbing":"false","isInsertCoverToMp4":"true","backgroundMusicNumber":0,"isSubtitles":"true","haveInCommerical":0}
        return self.s.post(self.video, json=body)

