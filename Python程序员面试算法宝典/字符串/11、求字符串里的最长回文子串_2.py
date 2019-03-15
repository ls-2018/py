"""
前一种方法可以看成是一种n*n的算法
并且开辟了一个N*N的空间



#  方法二: 中心扩展法
分奇数和偶数,两种情况


时间复杂度  n*n
空间复杂度   1
"""


class Test:
    def __init__(self):
        self.startIndex = 0
        self.lens = 0

    def getStartIndex(self):
        return self.startIndex

    def getLen(self):
        return self.lens

    def expandBothSide(self, strs, c1, c2):
        """
            对字符串str,以c1和c2为中心向两侧扩展寻找回文子串
        """
        n = len(strs)
        while c1 >= 0 and c2 <= n and list(strs)[c1] == list(strs)[c2]:
            c1 -= 1
            c2 += 1
        # 扩展玩后不匹配,要收缩回来
        tmpStartIndex = c1 + 1

        tmpLen = c2 - c1 - 1
        if tmpLen > self.lens:
            self.lens = tmpLen
            self.startIndex = tmpStartIndex

    def getLongestPalindrome(self, strs):
        if strs is None:
            return
        n = len(strs)
        if n < 1:
            return
        i = 0
        while i < n - 1:
            # 找回文字符串长度为奇数的情况(第i个字符向两边扩展)
            self.expandBothSide(strs, i, i)
            # 找回文字符串长度为偶数的情况(第i和i+1个字符向两边扩展)
            self.expandBothSide(strs, i, i + 1)
            i += 1

        # 这种是每个字符都向两边扩展,找最佳


if __name__ == '__main__':
    strs = 'abcdefgedxyz'
    t = Test()
    t.getLongestPalindrome(strs)
    if t.getStartIndex() != -1 and t.getLen() != -1:
        print('最长字符串为:')
        i = 0
        while i < t.getStartIndex() + t.getLen() - 1:
            print(list(strs)[i], end=' ')
            i += 1
    else:
        print('查找失败')
