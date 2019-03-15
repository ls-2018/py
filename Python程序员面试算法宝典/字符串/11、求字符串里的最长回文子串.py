"""
对于一个字符串假定P(I,J)=1 表示字符串中从i到j是回文字符串,  为0不是

那么P(i,i) = 1


"""


class Test:
    def __init__(self):
        self.startIndex = None
        self.lens = None

    def getStartIndex(self):
        return self.startIndex

    def getLen(self):
        return self.lens

    def getLongestPalindrome(self, strs):
        if strs is None:
            return
        n = len(strs)  # 字符串的长度
        if n < 1:
            return
        self.startIndex = 0
        self.lens = 1

        # 申请额外的存储空间记录查找的历史信息
        historyRecord = [([0] * n) for i in range(n)]

        # 初始化长度为1的回文字符串信息
        i = 0
        while i < n:
            historyRecord[i][i] = 1  # 对角线为1
            i += 1

        # 初始化长度为2的回文字符串信息
        i = 0
        while i < n - 1:
            if list(strs)[i] == list(strs)[i + 1]:
                historyRecord[i][i + 1] = 1
                self.startIndex = i  # 记录最后一次
                self.lens = 2
            i += 1
        # 查找长度大于等于3的回文字符串
        pLen = 3    # 起始长度
        while pLen < n:  # 字符串的长度
            i = 0
            while i < n - pLen + 1:
                j = i + pLen - 1    # 回文字符串的最后一个字符
                if list(strs)[i] == list(strs)[j] and historyRecord[i + 1][j - 1] == 1:   # 为什有这一步,因为需要用到长度为2
                    historyRecord[i][j] = 1
                    self.startIndex = i
                    self.lens = pLen
                i += 1
            pLen += 1
            #


if __name__ == '__main__':

    strs = 'abcdefgfedcxyz'
    t = Test()
    t.getLongestPalindrome(strs)
    if t.getStartIndex() != -1 and t.getLen() != -1:
        print('最长回文字符串为:', )
        i = t.getStartIndex()
        while i < t.getStartIndex() + t.getLen():
            print(list(strs)[i], end=' ')
            i += 1
    else:
        print('查找失败')
