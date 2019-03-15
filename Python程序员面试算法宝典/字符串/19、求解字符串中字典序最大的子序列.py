"""
字典最大的子序列是这样构造的:
字符串a0....a(n-1)
    从中找到最大的字符ai
    在a(i+1)....a(n-1)找到最大的字符ak
    知道要找的字符串长度为0
"""


# 顺序遍历法
def func_1(src):
    """
    时间复杂度   N*N
    空间复杂度   N
    """
    if src is None:
        return None

    lens = len(src)
    longestSub = [None] * lens
    k = i = 0
    while i < lens:
        longestSub[k] = list(src)[i]
        j = i + 1
        while j < lens:  # 遍历一次找到最大的.
            # 找出第i个字符后面最大的字符放到largestSUb[k]中
            if list(src)[j] > longestSub[k]:
                longestSub[k] = list(src)[j]
                i = j
            j += 1
        k += 1
        i += 1
    return ''.join(longestSub[0:k])


# 逆序遍历法
def func_2(src):
    """
    不管什么序列,最后一个字符始终会有,
    接着遍历只要  大于或等于  首字母的  就添加到子串首

    时间复杂度  N
    空间复杂度  N
    """
    if src is None:
        return None
    lens = len(src)
    largestSub = [None] * lens
    # 最后一个字符一定在子串中
    largestSub[0] = list(src)[lens - 1]
    i = lens - 2  # 倒是第二个开始
    j = 0
    # 逆序遍历字符串
    while i > 0:
        if ord(list(src)[i]) >= ord(largestSub[j]):
            j += 1
            largestSub[j] = list(src)[i]
        i -= 1
    largestSub = largestSub[0:j + 1]

    # 逆序
    i = 0
    while i < j:
        tmp = largestSub[i]
        largestSub[i] = largestSub[j]
        largestSub[j] = tmp
        i += 1
        j -= 1

    return ''.join(largestSub)


if __name__ == '__main__':
    s = 'acbdxmng'
    print(func_1(s))
    print(func_2(s))
