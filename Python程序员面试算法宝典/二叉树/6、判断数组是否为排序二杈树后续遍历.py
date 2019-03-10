"""
左孩子比根节点小
右孩子比根节点大
"""


def IsAfterOrder(arr, start, end):
    if arr == None:
        return False
    # 如果是后续(左右中)遍历,最后一个肯定是根节点
    root = arr[end]
    # 找到第一个大于root的值,那么前面所有的所有的结点都位于root的左子树上
    i = start
    while i < end:
        if (arr[i] > root):
            break
        i += 1
    # 如果序列是后续遍历的序列,那么从i开始的所有值都应该大于根节点root的值
    j = i
    while j < end:
        if arr[j] < root:
            return False
        j += 1

    left_IsAfterOrder = True
    right_IsAfterOrder = True

    # 判断大于root值的序列是否是某一二元查找树的后序遍历
    if i > start:
        left_IsAfterOrder = IsAfterOrder(arr, start, i - 1)
    # 判断大于root值的序列是否某一二元查找树的后序遍历
    if j < end:
        right_IsAfterOrder = IsAfterOrder(arr, i, end)
    return left_IsAfterOrder and right_IsAfterOrder


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 7, 6, 4, ]
    result = IsAfterOrder(arr, 0, len(arr) - 1)

    if result:
        print('√')
    else:
        print('×')
