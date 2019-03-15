"""
前面的这种方法,需要对奇数和偶数单独处理

# 方法三:Manacher算法
通过向相邻字符中插入一个分隔符,把回文字符串的长度都变为奇数,从而对这两种情况统一处理.
aba ---->*a*b*a*
aa  ----->*a*a*

主要思路:
    1、在字符串中相邻的字符中插入分隔符,字符串的首尾也插入分割字符(字符串中不存在的字符,本例以字符*作为分割字符)
    2、用一个额外的辅助数组P来记录以每个字符为中心对应的回文字符串的信息.
    3、P[i]记录了以字符串的长度为2*P[i]-1,P[i]-1就是这个回文字符串在原来字符串中的长度.

例如 *a*b*a*对应的辅助数组P为[1,2,1,4,1,2,1]最大值为P[3]=4----->原回文字符串的长度为4-1=3


艹,这种看不懂
"""


class Test:
    def __init__(self):
        self.center = None
        self.palindromeLen = None

    def getCenter(self):
        return self.center

    def getLen(self):
        return self.palindromeLen

    def mins(self, a, b):
        """求较小值"""
        return b if a > b else a

    def Manacher(self, strs):
        """
        找出字符串最长的回文字符串
        :param strs:
        :return: 如果长度为偶数,那么表示中间偏左的那个字符的位置
        """
        lens = len(strs)  # 字符串的长度
        newLen = 2 * lens + 1
        s = ["*"] * newLen  # 插入分割符后的字符串
        p = [0] * newLen
        id = 0  # id表示以第id个字符为中心的回文字符串最右下端的小标志最大
        i = 0
        while i < lens:
            s[(i + 1) * 2] = list(strs)
            i += 1
        self.center = -1
        self.palindromeLen = -1
        # 求解p数组
        i = 1
        while i < newLen:
            if id + p[id] > i:
                p[i] = self.mins(id + p[id] - 1, p[2 * id - i])
            else:
                p[i] = 1
            # 然后接着向左右两边扩展求最长的回文子串
            while i + p[i] < newLen and i - p[i] > 0 and s[i - p[i]] == s[i + p[i]]:
                p[i] += 1
            # 当前求出的回文字符串的最右端的下标更大
            if i + p[i] > id + p[id]:
                id = i
            # 当前求出的回文字符串更长
            if p[i] - 1 > self.palindromeLen:
                self.center = (i + 1) // 2 - 1
                self.palindromeLen = p[i] - 1  # 更新最长回文子串的长度
            i += 1


if __name__ == '__main__':
    strs = "abcbax"

    t = Test()
    t.Manacher(strs)
    center = t.getCenter()
    palindromeLen = t.getLen()
    if center != -1 and palindromeLen != -1:
        print('最长回文子串为:')
        if palindromeLen % 2 == 1:
            i = center - palindromeLen // 2
            while i <= center + palindromeLen // 2:
                print(list(strs)[i], end=' ')
                i += 1
        else:
            # 回文字符串长度为偶数
            i = center - palindromeLen // 2
            while i <= center + palindromeLen // 2:
                print(list(strs)[i], end=' ')
                i += 1
    else:
        print('查找失败')
