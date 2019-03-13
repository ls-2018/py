"""
不是完全有这个子字符串，而是字符串中的元素是否完全都有
"""

# 直接法
def isContain(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        # 字符串str1 比str2 短
        i = 0
        while i < len1:
            j = 0
            while j < len2:
                if list(str1)[i] == list(str2)[j]:
                    break
                j += 1
            if j >= len2:
                return False
            i += 1
    else:
        # 字符串str2 比str1 短
        i = 0
        while i < len2:
            j = 0
            while j < len1:
                if list(str1)[j] == list(str2)[i]:
                    break
                j += 1
            if j >= len1:
                return False
            i += 1

    return True

if __name__ == '__main__':
    str1 = 'abcdef'
    str2 = 'abdcg'
    iscontain = isContain(str1, str2)
    if iscontain:
        print('包含')
    else:
        print('不包含')
