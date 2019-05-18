# a = {1, 2, 3}
#
# print(a.add(2))
#
# dict().fromkeys([1, 2, 3], 0)
# import json
#
# demo = {
#     'name': 1,
#     'age': 123
# }
# print(json.dumps(demo))
#
# import collections
#
# # d = collections.OrderedDict()
# d = dict()
# d[3] = 'A'
# d[2] = 'B'
# d[1] = 'C'
#
# for k, v in d.items():
#     print(k, v)
# text = json.dumps(d)
# print(text)
# print(json.loads(text, object_pairs_hook=collections.OrderedDict))
# # 3.6之后默认字典有序
#
# sum([i for i in range(100)])