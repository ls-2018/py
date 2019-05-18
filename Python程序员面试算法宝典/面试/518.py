x = "abc"
y = "def"
z = ["d", "e", "f"]
print(x.join(y))
print(x.join(z))
print(int('1'))
# print(int('1.1'))# 报错ValueError
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])  # 试图访问一个列表的以超出列表长度数作为开始索引的切片将不会导致 IndexError，并且将仅仅返回一个空列表


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
print('-----------------------------------------')
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(A0)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(10)  # 生成器
print(A1)  # range(0, 10)
A2 = [i for i in A1 if i in A0]
print(A2)  # []
A3 = [A0[s] for s in A0]
print(A3)  # [1, 2, 3, 4, 5]
A4 = [i for i in A1 if i in A3]
print(A4)  # [1, 2, 3, 4, 5]
A5 = {i: i * i for i in A1}
print(A5)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[i, i * i] for i in A1]
print(A6)  # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
print('----------------------')


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f(2)
f(3, [3, 2, 1])
f(3)
print('----------------------')
