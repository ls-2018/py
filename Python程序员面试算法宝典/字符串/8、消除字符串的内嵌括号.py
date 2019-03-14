"""
strs = "(1,(2,3),(4,(5,6),7)"
把上面的表达式变成(1,2,3,4,5,6,7)



一、判断字符串是否合法
二、消除表达式中的括号

"""


def remove(strs):
    if strs is None:
        return strs

    parent_num = 0  # 用来记录不匹配的 ”（“出现的次数
    if list(strs)[0] != "(" or list(strs)[-1] != ")":
        return None
    sb = '('
    # 字符串首尾的括号可以单独处理
    i = 1
    while i < len(strs) - 1:
        ch = list(strs)[i]
        if ch == '(':
            parent_num += 1
        elif ch == ')':
            parent_num -= 1
        else:
            sb += list(strs)[i]
        i += 1
    # 判断括号是否正确
    if parent_num != 0:
        print('括号不匹配')
        return None
    # 处理字符串结尾的‘）’
    sb += ')'
    return sb


if __name__ == '__main__':
    strs = "(1,(2,3),(4,(5,6),7))"
    print(remove(strs))
