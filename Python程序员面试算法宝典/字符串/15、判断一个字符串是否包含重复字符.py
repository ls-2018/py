"""

"""


# 方法一: n*n
def isDup(strs):
    n = len(strs)
    j = 0
    for i in range(n):
        j = i + 1
        while j < n:
            if list(strs)[i] == list(strs)[j]:
                return '有重复字符'
            j += 1
    return '没有重复字符'


# 方法二:
def isDup_2(strs):
    """
    常见字符共有256个
    时间复杂度为  N
    空间复杂度为  8
    """
    lens = len(strs)
    flags = [0] * 8  # 假设32为机器,只需要8个32 位的int,8*32=256
    i = 0
    while i < lens:
        index = ord(list(strs)[i]) // 32
        shift = ord(list(strs)[i]) % 32
        if (flags[index] & (1 << shift)) != 0:  # 判断是否已经赋值了
            return '有重复字符'
        flags[index] |= (1 << shift)  # 没有的情况下,进行赋值
        i += 1  # 否则第二次循环时i没变

    return '没有重复字符'


if __name__ == '__main__':
    strs = 'gd'
    print(isDup(strs))
    print(isDup_2(strs))
