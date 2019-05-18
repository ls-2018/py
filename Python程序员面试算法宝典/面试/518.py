# x = "abc"
# y = "def"
# z = ["d", "e", "f"]
# print(x.join(y))
# print(x.join(z))
# print(int('1'))
# # print(int('1.1'))# 报错ValueError
# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])  # 试图访问一个列表的以超出列表长度数作为开始索引的切片将不会导致 IndexError，并且将仅仅返回一个空列表
#
#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)
# print('-----------------------------------------')
# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# print(A0)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# A1 = range(10)  # 生成器
# print(A1)  # range(0, 10)
# A2 = [i for i in A1 if i in A0]
# print(A2)  # []
# A3 = [A0[s] for s in A0]
# print(A3)  # [1, 2, 3, 4, 5]
# A4 = [i for i in A1 if i in A3]
# print(A4)  # [1, 2, 3, 4, 5]
# A5 = {i: i * i for i in A1}
# print(A5)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# A6 = [[i, i * i] for i in A1]
# print(A6)  # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# print('----------------------')
#
#
# def f(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
#
# f(2)
# f(3, [3, 2, 1])
# f(3)
# print('----------------------')
#
#
# class A(object):
#     def go(self):
#         print("go A go!")
#
#     def stop(self):
#         print("stop A stop!")
#
#     def pause(self):
#         raise Exception("Not Implemented")
#
#
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print("go B go!")
#
#
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print("go C go!")
#
#     def stop(self):
#         super(C, self).stop()
#         print("stop C stop!")
#
#
# class D(B, C):
#     def go(self):
#         super(D, self).go()
#         print("go D go!")
#
#     def stop(self):
#         super(D, self).stop()
#         print("stop D stop!")
#
#     def pause(self):
#         print("wait D wait!")
#
#
# class E(B, C):
#     pass
#
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()
# ########################################################33
# print(0, 0 == (0, False))
# print(id(0))
# print(id(False))
# print((0, 0) == 0, 0)
# print(0, 0 == (0, 0))
# a = 0, 0
# b = (0, 0)
# print(a == b)
# 换种写法,标明优先级
# print((((0, 0) == 0), 0))  # results in a two element tuple: (False, 0)
# print((0, (0 == (0, 0))))  # results in a two element tuple: (0, False)
# print(((0, 0) == (0, 0)))  # results in a boolean True # ALSO:
# a = 0, 0
# b = (0, 0)
# print(a == b)  # results in a boolean True
# 逗号分隔符与相等运算符的优先级是不同的。
# ##############################################################
'''
def func():
    a = 42
    return a


def func2():
    return 42


from dis import dis

dis(func)
dis(func2)
# 运行速度也是第二种快一
'''

'''
print(2 == True)
a = (1, 2, 3)

print(a.__sizeof__())
b = [1, 2, 3]
print(b.__sizeof__())
print(a.__len__())
print(b.__len__())
# 两种数据类型结构不同，list多存储了一个申请内存的槽的个数
'''
p = [1, 2, 3]
*x, = p
print(x == p)   # 都指向同一份内存
print(x is p)
y, *x = p
print(y)
print(*x)
x = p
print(x == p)
print(x is p)
