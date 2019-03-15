"""
字典最大的子序列是这样构造的:
字符串a0....a(n-1)
    从中找到最大的字符ai
    在a(i+1)....a(n-1)找到最大的字符ak
    知道要找的字符串长度为0
"""


# 顺序遍历法
def func_1(src):
    if src is None:
        return None

    lens = len(src)
    longestSub = [None] * (lens + 1)
    k = i = 0
    while i < lens:
        longestSub[k] = list(src)[i]
        j = i + 1
        while j < lens: # 遍历一次找到最大的.
            # 找出第i个字符后面最大的字符放到largestSUb[k]中
            if list(src)[j] > longestSub[k]:
                longestSub[k] = list(src)[j]
                i = j
            j += 1
        k += 1
        i += 1
    return ''.join(longestSub[0:k])


if __name__ == '__main__':
    s = 'acbdxmng'
    result = func_1(s)
    if result is None:
        print("字符串为空")
    else:
        print(result)
