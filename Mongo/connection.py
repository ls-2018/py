import pymongo

mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)

MONGO = mongo_client['test']  # 选择数据库,不管有没有，都可以选到
print(MONGO)
# Database(MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True), 'test')
res = MONGO.userinfo.find({})  # 指定表。
print(res)  # <pymongo.cursor.Cursor object at 0x000001CE3ED88198>
res = list(res)
print(res)
# [{'_id': ObjectId('5ca83548763624c1418c1775'), 'name': 'xx'}, ]   ObjectId对象不可以被序列化
print(type(res[0]))  # 自动序列化为字典<class 'dict'>

# 由5ca83548763624c1418c1775字符串转换为ObjectID
# 当直接用_id = 5ca83548763624c1418c1775  查找数据时为NONE
from bson import ObjectId

ObjectId('5ca83548763624c1418c1775')

print(MONGO.userinfo.find({"$or": [{'name': 'dwb'}, {'age': 12}]}))

###############插入  #############
res = MONGO.userinfo.insert_one({'name': 'bs', 'age': 13})
print(res,res.inserted_id)  # 不用commit
# <pymongo.cursor.Cursor object at 0x000001F26AC87630>
# <pymongo.results.InsertOneResult object at 0x000001F26AC6B888> 5cad733cafd45c3ccc94404a

res = MONGO.userinfo.insert_many([{},])
print(res,res.inserted_ids)  # 不用commit  ,不再是字符串，而是对象