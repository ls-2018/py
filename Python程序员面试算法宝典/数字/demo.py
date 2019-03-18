from __future__ import unicode_literals

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
dic['a'].name = 'xxxx'
for k, v in dic.items():
    print(v.name, '--')
#
# def func1():
#     a = 10
#     def func_2():
#         print(a)
#     print(func_2.__closure__)  # ???????
#     return func_2()
#
# func1()

import sys

print(sys.getdefaultencoding())  # utf8
print('foo' + u'bar')

test = b'this is a pig'
print(type(test))
"""
文本字符串：（在Python2 中是 Unicode，在Python3 中是str）                  别名six.text_type
字节字符串：（在Python2 中是 str，    在Python3 中是bytes）                别名six.binary_type

decode  bytes解码
encode  str  编码
"""

text_str= 'Γεια σας, τον κόσμο'
# text_str= '测试'
print(type(text_str))
print(text_str.encode('utf8').decode('utf8'))
"""
<class 'bytes'>
<class 'str'>
b'\xce\x93\xce\xb5\xce\xb9\xce\xb1 \xcf\x83\xce\xb1\xcf\x82, \xcf\x84\xce\xbf\xce\xbd \xce\xba\xcf\x8c\xcf\x83\xce\xbc\xce\xbf'

文本字符串与字节字符串完全不同的字符串。 文本字符串的repr看上去更像是人类可读的希腊文，而字节字符串的repr看上去更像是机器可读的。


Unicode 是为了破除ASCII字节与字符1:1的对应关系 ;是ASCII的超集
一个Unicode可以为1-4个字节，
utf8 是变长的

因此如果尝试将一个自己字符串使用Latin-1编码而使用utf-8解码，会出问题
因此如果尝试将一个自己字符串使用utf-8编码而使用Latin-1解码，会乱码
"""
print(5/2)