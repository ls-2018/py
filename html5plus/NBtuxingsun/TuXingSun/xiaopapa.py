import requests
import time,os
from uuid import uuid4
from settings import MUSIC_PATH
from settings import IMAGE_PATH
from settings import MONGO_DB

XMLY_URL = "http://m.ximalaya.com/tracks/%s.json"


content_id_erge_list = ["/ertong/424529/7713675",
                   "/ertong/424529/7713660",
                   "/ertong/424529/7713647",
                   "/ertong/424529/7713577",
                   "/ertong/424529/7713571",
                   "/ertong/424529/7713544"]

content_id_gushi_list = [
    "/ertong/260744/139932898",
    "/ertong/260744/137850096"
]
def xiaopapaerge(content_id_erge_list):
    for item in content_id_erge_list:
        content_id = item.split("/")[-1]
        content_dict = requests.get(XMLY_URL%(content_id)).json()
        time.sleep(0.5)
        print(content_dict.get("title"))
        
        # 获取音频内容
        play_path = content_dict.get("play_path")
        music = requests.get(play_path).content
        music_name = f"{uuid4()}.mp3"
        music_path = os.path.join(MUSIC_PATH,music_name)
        with open(music_path,"wb") as mf:
            mf.write(music)
        
        # 获取图片内容
        cover_url = content_dict.get("cover_url")
        cover = requests.get(cover_url).content
        cover_name = f"{uuid4()}.jpg"
        cover_path = os.path.join(IMAGE_PATH,cover_name)
        with open(cover_path,"wb") as cf:
            cf.write(cover)
        
        music_info = {
            "title" : content_dict.get("title"),
            "author": content_dict.get("nickname"),
            "play_count" : 0,
            "intro" : content_dict.get("intro"),
            "tag" : "erge",
            "update_at":time.time(),
            "audio":music_name,
            "cover":cover_name
        }
    
        MONGO_DB.content.insert_one(music_info)


def xiaopapagushi(content_id_gushi_list):
    for item in content_id_gushi_list:
        content_id = item.split("/")[-1]
        content_dict = requests.get(XMLY_URL % (content_id)).json()
        time.sleep(0.5)
        print(content_dict.get("title"))
        
        # 获取音频内容
        play_path = content_dict.get("play_path")
        music = requests.get(play_path).content
        music_name = f"{uuid4()}.mp3"
        music_path = os.path.join(MUSIC_PATH, music_name)
        with open(music_path, "wb") as mf:
            mf.write(music)
        
        # 获取图片内容
        cover_url = content_dict.get("cover_url")
        cover = requests.get(cover_url).content
        cover_name = f"{uuid4()}.jpg"
        cover_path = os.path.join(IMAGE_PATH, cover_name)
        with open(cover_path, "wb") as cf:
            
            cf.write(cover)
        
        music_info = {
            "title": content_dict.get("title"),
            "author": content_dict.get("nickname"),
            "play_count": 0,
            "intro": content_dict.get("intro"),
            "tag": "gushi",
            "update_at": time.time(),
            "audio": music_name,
            "cover": cover_name
        }
        
        MONGO_DB.content.insert_one(music_info)
        


xiaopapaerge(content_id_erge_list)
xiaopapagushi(content_id_gushi_list)