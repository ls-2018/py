"""
对二叉树进行先序遍历，把遍历的路径记录下来，当遍历到叶子结点时，判断当前的路径上所有结点数据的和是否等于给定的整数，如果相等则输出路径信息。
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def constructTree(x):
    root = BiTNode()
    node1 = BiTNode()
    node2 = BiTNode()
    node3 = BiTNode()
    node4 = BiTNode()
    node5 = BiTNode()
    root.data = 6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = x
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    return root


def FindRoad(root, num, sums, v):
    """
    打印出满足所有结点数据的和等于num的所有路径
    :param root:
    :param num:
    :param sums:  当前结点和
    :param v:   路径信息
    :return:
    """
    sums += root.data
    v.append(root.data)

    # 当前结点是叶子结点且遍历的路径上所有结点的和等于num
    if root.lchild is None and root.rchild is None and sums == num:
        i = 0  # 也就是相当于在递归内部进行了打印
        while i < len(v):
            print(v[i])
            i += 1

    # 遍历root的左子树
    if root.lchild is not None:
        FindRoad(root.lchild, num, sums, v)

    if root.rchild is not None:
        FindRoad(root.rchild, num, sums, v)
    # 清除遍历的路径
    sums -= v[-1]
    v.remove(v[-1])


if __name__ == '__main__':
    root = constructTree(2)
    x = []
    print('满足路径结点和等于8的路径为：')
    FindRoad(root, 8, 0, x)
