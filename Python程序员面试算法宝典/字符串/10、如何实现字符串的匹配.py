"""
给定主字符串S与模式字符串P,判断P是否是S的子串,如果是,那么找出P在S中第一次出现的下标
"""
"""
方法一:
比较从主串S中以Si为首的字符串和模式串P,判断P是否为S的前缀,

如果是,那么P在S中第一次出现的位置则为i,否则接着比较从S(i+1)开始的子串与模式串P,
这种方法的时间复杂度为O(m*n),此外如果i>m-n,那么在主串中以Si为首的子串的长度必定小于模式串P的长度.

"""


def match(s, p):
    # 检查参数的合理性
    if s is None or p is None:
        print('参数不合理')
        return -1
    slen = len(s)
    plen = len(p)
    # p 肯定不是s的子串
    if slen < plen:
        return -1

    i = j = 0
    while i < slen and j < plen:
        if list(s)[i] == list(p)[j]:
            # 如果相同,那么继续比较后面的字符
            i += 1
            j += 1
        else:
            # 后退回去重新比较
            i = i - j + 1
            j = 0
            if i > slen - plen:  # 保证主串待匹配的字符数大于等于模式串剩余的字符数
                return -1
    if j >= plen:
        # 匹配成功
        return i - plen
    return -1


if __name__ == '__main__':
    s = 'xyzabcd'
    p = 'abc'
    print(match(s, p))
