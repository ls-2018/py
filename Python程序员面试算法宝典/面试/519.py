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

# a = 0.1 * 3
# b = 0.1 + 0.1 + 0.1
# print(a == b)
import os


def print_dir_contents(filepath):
    print(list(os.walk(filepath)))


if __name__ == '__main__':
    filepath = r'D:\Destop\book\Python程序员面试算法宝典'
    print_dir_contents(filepath)

demo = [('D:\\Destop\\book\\Python程序员面试算法宝典',
         ['链表', '面试'],
         ['fabfile.py', 'readme', '指令运行周期.py', '数据结构算法及知识点.md']),
        ('D:\\Destop\\book\\Python程序员面试算法宝典\\链表', [],
         ['１、链表的逆序.py', '１０、合并有序链表.py', '１１、只有单个结点的指针下删除该结点.py',
          '１２、如何判断两个单链表是否有交叉.py', '１３、 如何展开链接列表.py', '２、删除无序链表中的重复项.py',
          '３、计算两个单链表所代表的的数之和.py', '４、对链表重新排序.py', '５、找出单链表中倒数第K个元素.py',
          '６、将链表向右旋转k个位置.py', '７、如何检测一个单链表是否有环.py', '８、翻转链表相邻元素.py',
          '９、如何把链表以K个结点为一组进行翻转.py']),
        ('D:\\Destop\\book\\Python程序员面试算法宝典\\面试', [], ['518.py', '519.py'])
        ]


