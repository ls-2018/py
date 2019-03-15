"""
    a = 'D:/Destop/book/Python程序员面试算法宝典/字符串/22、求相对路径.py'

    b = 'D:/Destop/book/Python程序员面试算法宝典/链表/９、如何把链表以K个结点为一组进行翻转.py'

获取b相对于a的相对路径


找到相同的路径， 对于a中每一个目录结构，在b前面加../
   在添加b单独的路径

"""


def getRelativePath(path1, path2):
    if path1 is None or path2 is None:
        print('参数不合法')
        return
    relativePath = ''

    # 用来指向两个路径中不同目录的起始路径
    diff1 = 0
    diff2 = 0
    i = j = 0
    len1 = len(path1)
    len2 = len(path2)
    while i < len1 and j < len2:
        # 如果目录相同，那么往后遍历
        if list(path1)[i] == list(path2)[j]:
            if list(path1)[i] == '/':
                diff1 = i
                diff2 = j
            i += 1
            j += 1
        else:
            # 不同的目录
            # 把path1非公共部分的目录转换为../
            diff1 += 1  # 跳过目录分隔符  /
            while diff1 < len1:
                # 碰到下一级目录
                if list(path1)[diff1] == '/':
                    relativePath += '../'
                diff1 += 1
            # 把path2的非公共部分的路径加到后面
            diff2 += 1
            relativePath += path2[diff2:]
            break
    return relativePath


if __name__ == '__main__':
    a = 'D:/Destop/book/Python程序员面试算法宝典/字符串/22、求相对路径.py'

    b = 'D:/Destop/book/Python程序员面试算法宝典/链表/９、如何把链表以K个结点为一组进行翻转.py'

    print(getRelativePath(a, b))
