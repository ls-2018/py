#数据库配置
import pymongo
client = pymongo.MongoClient(host="127.0.0.1",port=27017)
MONGO_DB = client["TuXingSunDB"]


#目录配置
MUSIC_PATH = "Music"
IMAGE_PATH = "Image"