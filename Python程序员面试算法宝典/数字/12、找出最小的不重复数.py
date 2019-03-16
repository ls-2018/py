"""
给定一个正整数,求比这个数大且最小的  不重复数,不重复数:相邻的两位不相同,
例如   1101是重复数,
      1201是不重复数
"""
# 蛮力法
"""给指定的数加1,然后判断是不是重复数,如果不是,继续加1 """


# #######################   从右到左的贪心法    ############################################
def carry(num, pos):
    """
    处理数字相加的进位
    :param num: 字符数组
    :param pos: pos为进行加1 操作对应的下标位置
    :return:
    """
    while pos > 0:
        if int(num[pos]) > 9:
            num[pos] = '0'
            num[pos - 1] = str(int(num[pos - 1]) + 1)
        pos -= 1


def findMinNonDupNum(n):
    """
    获取大于n的最小不重复数
    :param n:
    :return: 大于n的最小不重复数
    """
    count = 0  # 用来记录循环次数
    nChar = list(str(n + 1))
    ch = [None] * (len(nChar) + 2)
    ch[0] = '0'
    ch[len(ch) - 1] = '0'
    i = 0
    while i < len(nChar):
        ch[i + 1] = nChar[i]
        i += 1
    lens = len(ch)
    i = lens - 2  # 从右向左遍历
    while i > 0:
        count += 1
        if ch[i - 1] == ch[i]:
            ch[i] = str(int(ch[i]) + 1)  # 末尾数字加1
            carry(ch, i)  # 处理进位
            # 把下标为i后面的字符串变成0101...串
            j = i + 1
            while j < lens:
                if (j - i) % 2 == 1:
                    ch[j] = '0'
                else:
                    ch[j] = '1'
                j += 1
            # 第i位加1后,可能会与第i+1位相等
            i += 1
        else:
            i -= 1
    print('循环次数为:', str(count))
    return int(''.join(ch))


if __name__ == '__main__':
    print(findMinNonDupNum(23345))
    print(findMinNonDupNum(1101010))
    print(findMinNonDupNum(99010))
    print(findMinNonDupNum(8989))
