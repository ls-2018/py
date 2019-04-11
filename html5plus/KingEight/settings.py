import pymongo

mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
MONGO=mongo_client['KingEight']
XPP_URL = 'https://m.ximalaya.com/tracks/%s.json'
