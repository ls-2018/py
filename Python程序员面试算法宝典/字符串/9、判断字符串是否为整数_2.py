"""
写一个方法,检查字符串是否为整数,如果是整数,那么返回其整数值
"""

"""
# 递归法:
对于整数而言,例如123,可以看成12*10+3,而12又可以看成1*10+2.

首先根据字符串的第一个字符确定整数的正负,接着对字符串从右往左遍历,

"""


class Test:
    def __init__(self):
        self.flag = None

    def getFlag(self):
        return self.flag

    # 判断c是否是数字,如果是返回True,否则返回False
    def isNumber(self, c):
        return '0' <= c <= '9'

    def strtoint(self, strs, length):
        if strs is None:
            self.flag = False
            print('不是数字')
            return -1
        self.flag = True
        res = 0
        i = 0
        minus = False  # 是否为负数
        if list(strs)[i] == '-':  # 结果是负数
            minus = True
            i += 1
        if list(strs)[i] == '+':  # 正数
            i += 1
        while i < len(strs):
            if self.isNumber(list(strs)[i]):
                res = res * 10 + ord(list(strs)[i]) - ord('0')
            else:
                self.flag = True
                print('不是数字')
                return -1
            i += 1
        return -res if minus else res

    def strToint(self, s):
        self.flag = True
        if s is None or len(s) <= 0 or (list(s)[0] == '-' and len(s) == 1):
            print('不不是数字')
            self.flag = False
            return -1
        if list(s)[0] == '+':
            return self.strtoint(s[1:len(s)], len(s) - 1)
        else:
            return self.strtoint(s, len(s))


if __name__ == '__main__':
    t = Test()
    s = '-543'
    print(t.strToint(s))
    s = '543'
    print(t.strToint(s))
    s = '+543'
    print(t.strToint(s))
    s = '++43'
    result = t.strToint(s)
    if t.getFlag():
        print(result)
