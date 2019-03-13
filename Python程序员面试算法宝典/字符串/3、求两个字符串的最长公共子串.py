# 方法一:动态规划
"""
首先定义二元函数f(i,j),表示分别以s1[i],s2[j]结尾的公共子串的长度，显然 f(0,j)=0(j>=0)
f(i,0)=0(i>=0),那么对于f(i+1,j+1)而言，则有如下两种取值
1、f(i+1,j+1) = 0,当str1[i+1]!=str2[j+1]
2、f(i+1,j+1)=f(i,j)+1,当str1[i+1]=str2[j+1]

"""


def getMaxSubStr(str1, str2):
    """
    获取两个字符串的最长子字符串
    :param str1:
    :param str2:
    :return:
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


"""
            len1
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
len2    [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]
 
"""
if __name__ == '__main__':
    print(getMaxSubStr('aszzzzzzzzzzzzzzzdc', 'aszzzzzzzzzzzzzzzdczzzzzzzzzzzzzzzz'))
