import pymongo
from bson import ObjectId

mongo_client = pymongo.MongoClient(host="127.0.0.1", port=27017)
MONGO = mongo_client["test"]

# 查询数据
res = list(MONGO.userinfo.find({}))
print(res)
res = MONGO.userinfo.insert_one({'name': "zhangsan "})
print(res)
