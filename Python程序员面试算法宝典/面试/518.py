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
# p = [1, 2, 3]
# *x, = p
# print(x == p)   # 都指向同一份内存
# print(x is p)
# y, *x = p
# print(y)
# print(*x)
# x = p
# print(x == p)
# print(x is p)


# encoding=utf-8
# 输入5个整数，排序后输出
# 算法：
# 1、从输入流获取5个整数，并存于列表中
# 2、调用列表的sort方法对列表进行排序
# 3、打印排序后的结果，打印排序之前的

# numList = []
# i = 1
# while i <= 5:
#     try:
#         n = int(input("请输入第%d个数" % i))
#     except ValueError as e:
#         print("输入的非数字类型数据，请重新输入。")
#         continue
#     else:
#         numList.append(n)
#         i += 1
# print(numList)
# tmpList = numList[:]
# tmpList.sort()
# print(numList)
# print(tmpList)

# # 2、使用尽可能多的方法实现list去重
# # list.count()
#
# 方法一：
# encoding=utf-8

# a = [1, 1, 3, 2, 2, 1, 5, 5, 3, 4]
# n = 0
# while n < len(a):
#     if a.count(a[n]) > 1:
#         a.remove(a[n])
#         continue
#     n += 1
#
# print(a)
#
#
# # 方法二：
#
# def listP(old_list):
#     tmpDict = dict.fromkeys(old_list, 0)
#     new_list = tmpDict.keys()
#     return new_list
#
#
# if __name__ == "__main__":
#     old_list = [1, 2, 3, 3, 4, 6, 4, 2, 7, 1]
#     new_list = listP(old_list)
#     print(old_list)
#     print(new_list)
#
#
# # 方法三：
#
# def listP(old_list):
#     return list(set(old_list))
#
#
# if __name__ == "__main__":
#     old_list = [1, 2, 3, 3, 4, 6, 4, 2, 7, 1]
#     new_list = listP(old_list)
#     print(old_list)
#     print(new_list)
#
#
# # 方法四：
#
# def listP(old_list):
#     map(lambda x, y: x if y in x else x + [y], [[]] + old_list)
#     return list(set(old_list))
#
#
# if __name__ == "__main__":
#     old_list = [1, 2, 3, 3, 4, 6, 4, 2, 7, 1]
#     new_list = listP(old_list)
#     print(old_list)
#     print(new_list)
#
#
# # 3、输入3个数字，以逗号隔开，输出其中最大的数
# def findMaxNum(x, y, z):
#     x, y, z = x, y, z
#     if x < y:
#         x, y = y, x
#     if x < z:
#         x, z = z, x
#     return x
#
#
# if __name__ == "__main__":
#     numList = input("请输入三个数，以逗号隔开：".encode("gbk")).split(",")
#     print(numList)
#     res = findMaxNum(int(numList[0]), int(numList[1]), int(numList[2]))
#     print(res)
#
# # 4、求两个正整数m和n的最大公约数
# # 方法一：
# a, b = input().split(",")
# a, b = int(a), int(b)
# c = a % b
# while c:
#     a, b = b, c
#     c = a % b
# print(b)
#
#
# # 方法二：
#
# def gcd(x, y):
#     min = y if x > y else x
#     for i in range(1, min + 1):
#         if x % i == 0 and y % i == 0:
#             gcd1 = i
#
#     return gcd1
#
#
# a = 64
# b = 24
# print(gcd(a, b))
#
# # 5、输入一个正整数，输出其阶乘结果
# # 方法一：  # encoding=utf-8
#
# num = int(input("请输入一个正整数：".encode("gbk")))
# result = 1
# for i in range(2, num + 1):
#     result *= i
# print("%d 的阶乘为：" % num, result)
#
# # 方法二：
# try:
#     num = int(input("请输入一个正整数：".encode("gbk")))
# except ValueError as  e:
#     print("请输入整数")
# else:
#     f = map(lambda x, y: x * y, range(1, num + 1))
#     print(f)
import re

demo = 'asd123afs'
# demo.replace()
res = re.findall('\d+', demo)
for i in res:
    demo = demo.replace(i, 'afanti')
print(demo)
