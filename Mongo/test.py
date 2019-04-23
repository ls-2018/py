import pymongo
from bson import ObjectId

mongo_client = pymongo.MongoClient(host="127.0.0.1", port=27017)
MONGO = mongo_client["test"]

# 查询数据
res = list(MONGO.userinfo.find({}))
print(res)

# res = MONGO.userinfo.find_one({"id":20})
# res["_id"] = str(res["_id"])

# res = list(MONGO.userinfo.find({"$or":[{"name":"dwb"},{"id":15}]}))
# print(res)

# ObjectId json操作
# res_obj = MONGO.userinfo.find_one({"_id":ObjectId(res["_id"])})
# print(res_obj)
# print(res.get("name"),type(res.get("_id")),type(res))
#
# import json
# res_json = json.dumps(res)
# print(res_json)


# 增加数据
# res = MONGO.userinfo.insert_one({"name":"pymongo","age":666})
# print(res,res.inserted_id)

# res = MONGO.userinfo.insert_many([{"name":"pymongo","age":666},{"name":"pymongo","age":666}])
# print(res,res.inserted_ids)

# for doc in res:
#     print(doc)

# 修改数据
# res = MONGO.userinfo.update_many({"age":666},{"$set":{"name":"pydwb","age":999}})
# print(res,dir(res),res.raw_result)

# 删除数据
# res = MONGO.userinfo.delete_one({"id":20})
# res = MONGO.userinfo.delete_many({"name":1})
# print(res,dir(res),res.raw_result)


# skip sort limit

# res = list(MONGO.userinfo.find({}).limit(5))
# print(len(res))

# res = list(MONGO.userinfo.find({}).limit(5).skip(5))
# print(len(res),res)

# res = list(MONGO.userinfo.find({}).sort("age",pymongo.DESCENDING))
# print(res)


# res = list(MONGO.userinfo.find({}).sort("age",pymongo.DESCENDING).skip(5).limit(2))
# print(res)


# python 的 update
# res = MONGO.userinfo.find_one({"name":"200wansui"})
# print(res)
# res.get("info")["shengao"] = 170
# res.get("info")["tizhong"] = 130
# res.get("info")["long"] = 18.5

# MONGO.userinfo.update_one({"_id":res.get("_id")},{"$set":res})
# res = MONGO.userinfo.find_one({"name":"200wansui"})
# print(res)
