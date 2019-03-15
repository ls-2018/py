"""
给出一个字符串数组,找出最长的字符串,使其能由数组中其他的字符串组成
例子:
    ['test','tester','apple',''....'testbattingcat','cat','batting']

满足题目要求的字符串为 testbattingcat  ,因为这个字符串可以由数组中的字符串 test  batting cat 组成

1、  找最长数组,先排序
2、  在对每一个字符串,判断是否可以由其他字符串拼接成
"""


class LongestWord:

    def isContain(self, strArray, word, length):
        """
        判断字符串Word是否能由数组strArray 中的其他单词组成
        :param strArray:
        :param word:    待判断的后缀子串
        :param length: 待判断的后缀子串的长度
        :return:
        """
        lens = len(word)
        # 递归的结束条件,当字符串长度为0时,说明字符串已经遍历完了
        if lens == 0:
            return True
        # 循环取字符串的所有前缀
        i = 1
        while i <= lens:
            if i == length:
                return False
            strs = word[0:i]
            if strs in strArray:  # 判断字符串strs是否在字符串数组中
                # 查找完字符串的前缀后,递归判断后面的子串能否由其他单词组成
                if self.isContain(strArray, word[i:], length):
                    return True
            i += 1
        return False

    def getLogestStr(self, strArray):
        """找出能由数组中其他字符串组成的最长字符串"""
        # 对字符串由大到小排序
        strArray = sorted(strArray, key=len, reverse=True)
        print(strArray)

        # 贪心匹配
        i = 0
        while i < len(strArray):
            if self.isContain(strArray, strArray[i], len(strArray[i])):
                return strArray[i]
            i += 1
        # 如果没找到返回空
        return None


if __name__ == '__main__':
    strArray = ['test', 'tester', 'apple', '', 'testbattingcat', 'cat', 'batting']
    lw = LongestWord()
    longest = lw.getLogestStr(strArray)
    if longest is not None:
        print('最长字符串为:', longest)
    else:
        print('不存在这样的字符串')
