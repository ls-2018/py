"""
哈希一种算法，尽可能不重复
解决哈希冲突：
"""


class Student:
    def __init__(self, a, age):
        self.name = a
        self.age = age

    def __str__(self):
        return self.name

    def __hash__(self):
        return self.age


s = Student('ZHANGSAN', 22)
# print(hash(s))

'''
小数据池
int -5~256
str 大部分直接声明的字符串都会驻留
bool 很早就驻留了
目的：快速创建对象，节省内存
'''
a = 5
b = 5
print(id(a))
print(id(b))
# 1853131280
# 1853131280


"""
Python
    is  内存地址
    ==  值
JS
    === 值和类型
JAVA
    equals()    值
    ==          内存地址
"""
dic = dict.fromkeys('abc', s)
dic['a'].name='xxxx'
for k,v in dic.items():
    print(v.name,'--')