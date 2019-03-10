class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


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


def FindParentNode(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root
    lchild = FindParentNode(root.lchild, node1, node2)
    rchild = FindParentNode(root.rchild, node1, node2)
    # root 的左子树上没有结点node1 node2 ,那么一定在右子树上
    if lchild is None:
        return rchild
    elif rchild is None:
        return lchild
    else:
        return root


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(arr, 0, len(arr) - 1)
    node1 = root.lchild.lchild.lchild
    node2 = root

    res = FindParentNode(root, node1, node2)
    if res is not None:
        print(node1.data, node2.data, '最近的公共父结点为：', res.data)
    else:
        print('没有公共父结点')
