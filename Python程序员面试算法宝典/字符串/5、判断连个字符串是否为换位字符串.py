"""
相同字符，但位置不同

aaaabbc与abcbaaa就是换位字符串
"""


def compare(s1, s2):
    result = True
    bcount = [None] * 256
    i = 0
    while i < 256:
        bcount[i] = 0
        i += 1
    i = 0
    while i < len(s1):
        bcount[ord(list(s1)[i]) - ord('0')] += 1
        i += 1
    i = 0
    while i < len(s2):
        bcount[ord(list(s2)[i]) - ord('0')] -= 1
        i += 1
    i = 0
    while i < 256:
        if bcount[i] != 0:
            result = False
            break
        i += 1
    return result


if __name__ == '__main__':
    str1 = 'aaaabbc'
    str2 = 'cbbaaaa'
    if compare(str1, str2):
        print('是换位字符串')
    else:
        print('不是')
