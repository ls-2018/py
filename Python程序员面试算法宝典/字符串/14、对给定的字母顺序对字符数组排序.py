"""
已知字母序列[d,g,e,c,f,b,o,a]  轻松换一个方法,对输入的一组字符串['bed','dog','dear','eye']按照字母顺序排序病打印
本例输出  dear  dog  eye  bed
"""


def compare(str1, str2, char_to_int):
    len1 = len(str1)
    len2 = len(str2)
    i = j = 0
    while i < len1 and j < len2:
        # 如果字符不在给定的序列中,那么把值赋为-1
        if list(str1)[i] not in char_to_int.keys():
            char_to_int[list(str1)[i]] = -1

        if list(str2)[i] not in char_to_int.keys():
            char_to_int[list(str2)[i]] = -1
        # 比较各个字符的大小
        if char_to_int[list(str1)[i]] < char_to_int[list(str2)[j]]:
            return -1
        elif char_to_int[list(str1)[i]] > char_to_int[list(str2)[j]]:
            return 1
        else:
            i += 1
            j += 1
        if i == len1 and j == len2:
            return 0
        elif i == len1:
            return -1
        else:
            return 1


def insertSort(s, char_to_int):
    # 对字符数组进行排序
    # {'d': 0, 'g': 1, 'e': 2, 'c': 3, 'f': 4, 'b': 5, 'o': 6, 'a': 7}
    lens = len(s)
    i = 1
    while i < lens:
        temp = s[i]
        j = i - 1
        while j > 0:
            # 用给定的规则比较字符串的大小
            if compare(temp, s[j], char_to_int) == -1:
                s[j + 1] = s[j]
            else:
                break
            j -= 1
        s[j + 1] = temp
        i += 1


if __name__ == '__main__':
    s = ['bed', 'dog', 'dear', 'eye']
    sequence = 'dgecfboa'
    lens = len(sequence)
    # 用来存储字母序列与其对应的值的键值对
    char_to_int = dict()
    # 根据给定的字符序列构造字典
    i = 0
    while i < lens:
        char_to_int[list(sequence)[i]] = i
        i += 1
    print(char_to_int)
    insertSort(s, char_to_int)
    print(s)
