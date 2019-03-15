"""
demo = 'dabcdea'
# 方法一
    先将demo排序,在与demo求最长公共子序列
# 动态规划
    以第i个元素为结尾的最长递增子序列只与以第i-1个元素为结尾的最长递增子序列有关

    1、第i个元素单独作为一个子串   L[i]<=L[i-1]
    2、以第i-1个元素为结尾的最长递增子序列加1   (L[i]>L[i-1])

    ----->
        maxLen[i] = max(1, maxLen[j]+1)    j<i   and L[j]<L[i]
        maxLen[0]=1

"""


def getMax(strs):
    maxlen = 1
    lens = len(strs)
    for i in range(lens):
        j = i
        while j < lens - 2:
            if list(strs)[j + 1] <= list(strs)[j]:
                break
            j += 1
            if maxlen < j - i + 1:
                maxlen = j - i + 1
    return maxlen

    # maxLen = [None] * lens
    # maxLen[0] = 1
    # maxAscendingLen = 1
    # for i in range(lens):
    #     maxLen[i] = 1  # 最小值为1
    #     j = 0
    #     while j < i:
    #         if list(strs)[j] < list(strs)[i] and maxLen[j] > maxLen[i] - 1:
    #             maxLen[i] = maxLen[j] + 1
    #             maxAscendingLen = maxLen[i]
    #         j += 1
    # return maxAscendingLen


if __name__ == '__main__':
    s = 'xabcda'
    print(getMax(s))
