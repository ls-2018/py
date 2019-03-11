"""
二叉排序树，最小值在左下角；最大值在右下角
    f = (min + max)/2
    再进行中序遍历，如果当前结点值小于f，那么在这个节点的右子树中接着遍历，
                    否则遍历这个结点的左子树
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def getMinNode(root):
    """
    查找最小值的结点
    :param root:
    :return:
    """
    if root is None:
        return None
    while root.lchild is not None:
        root = root.lchild
    return root


def getMaxNode(root):
    """
    查找最大值的结点
    :param root:
    :return:
    """
    if root is None:
        return None
    while root.rchild is not None:
        root = root.rchild
    return root


def getNode(root):
    maxNode = getMaxNode(root)
    minNode = getMinNode(root)
    mid = (maxNode.data + minNode.data) / 2
    result = None
    while root is not None:
        if root.data <= mid:  # 小于等于
            root = root.rchild
        else:
            result = root
            root = root.lchild
    return result


def arraytotree(arr, start, end):
    if start <= end:
        root = BiTNode()
        mid = (start + end + 1) // 2
        root.data = arr[mid]
        root.lchild = arraytotree(arr, start, mid - 1)
        root.rchild = arraytotree(arr, mid + 1, end)
    else:
        root = None
    return root


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = arraytotree(arr, 0, len(arr) - 1)
    print(getNode(root).data)

"""
"""