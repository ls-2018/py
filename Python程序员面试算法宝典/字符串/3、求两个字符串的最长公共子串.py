"""
    首先定义二元函数f(i,j),表示分别以s1[i],s2[j]结尾的公共子串的长度，显然 f(0,j)=0(j>=0)
    f(i,0)=0(i>=0),那么对于f(i+1,j+1)而言，则有如下两种取值
    1、f(i+1,j+1) = 0,当str1[i+1]!=str2[j+1]
    2、f(i+1,j+1)=f(i,j)+1,当str1[i+1]=str2[j+1]


"""


# 方法一:动态规划
def getMaxSubStr(str1, str2):
    """
    获取两个字符串的最长子字符串
                len1
        [0, 0, 0, 0],
        [0, 0, 0, 0],
len2    [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    缺点:额外开辟了m*n的空间
    """
    len1 = len(str1)
    len2 = len(str2)
    sb = ''
    maxs = 0  # 用来记录最长的公共子串的长度
    maxI = 0  # 最长的公共子串的长度最后一个字符的位置
    # 申请新的空间来记录公共子串长度信息
    M = [([0] * (len1 + 1)) for i in range(len2 + 1)]
    # i = 0
    # while i < len2 + 1:
    #     M[i][0] = 0
    #     i += 1
    # j = 0
    # while j < len1 + 1:
    #     M[0][j] = 0
    #     j += 1

    # 利用递归公式填写新建的二维数组（公共子串的长度信息）
    i = 1
    while i < len2 + 1:
        j = 1
        while j < len1 + 1:

            if list(str1)[j - 1] == list(str2)[i - 1]:
                M[i][j] = M[i - 1][j - 1] + 1
                if M[i][j] >= maxs:
                    maxs = M[i][j]  # 子串的长度
                    maxI = i  # 记录str1中字符串的结尾位置
            # else:
            #     M[i][j] = 0
            j += 1
        i += 1
    # 找出公共子串
    i = maxI - maxs  # 起始位置
    while i < maxI:
        sb = sb + list(str1)[i]
        i += 1

    return sb


# 方法二:滑动比较法
def getMaxSubStr_2(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    maxLen = 0
    tmpMaxLen = 0
    maxLenEnd1 = 0
    sb = ''
    i = 0
    while i < len1 + len2:
        s1begin = s2begin = 0
        tmpMaxLen = 0
        if i < len1:
            s1begin = len1 - i
        else:
            s2begin = i - len1
        j = 0
        while (s1begin + j < len1) and (s2begin + j < len2):
            if list(s1)[s1begin + j] == list(s2)[s2begin + j]:
                tmpMaxLen += 1
            else:
                if tmpMaxLen > maxLen:
                    maxLen = tmpMaxLen
                    maxLenEnd1 = s1begin + j
                else:
                    tmpMaxLen = 0
            j += 1
        if tmpMaxLen > maxLen:
            maxLen = tmpMaxLen
            maxLenEnd1 = s1begin + j
        i += 1
    i = maxLenEnd1 - maxLen
    while i < maxLenEnd1:
        sb += list(s1)[i]
        i += 1
    return sb


if __name__ == '__main__':
    # print(getMaxSubStr('aszzzzzzzzzzzzzzzdc', 'aszzzzzzzzzzzzzzzdczzzzzzzzzzzzzzzz'))
    print(getMaxSubStr_2('aszzzzzzzzzzzzzzzdc', 'aszzzzzzzzzzzzzzzdczzzzzzzzzzzzzzzz'))
