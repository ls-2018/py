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
