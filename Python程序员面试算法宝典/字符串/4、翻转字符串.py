def reverseStr(str):
    ch = list(str)
    lens = len(ch)

    i = 0
    j = lens - 1
    while i < j:
        tmp = ch[i]
        ch[i] = ch[j]
        ch[j] = tmp

        i += 1
        j -= 1
    return ''.join(ch)


if __name__ == '__main__':
    str = 'abcdefg'
    print(str)
    print(reverseStr(str))


"""
另一种方法
how are you
uoy era woh
you are how
"""