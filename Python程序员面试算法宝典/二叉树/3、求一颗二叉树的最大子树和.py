"""
        6
    3       -7
-1    9

在上面这个图中,首先遍历结点-1 ,这个子树的最大值为-1 ,同理,当遍历到结点9时,子树的最大值为9,当遍历到结点3时,这个结点与其左右孩子结点值的和=11,大于最大值9
    因此最大的子树为以3为根节点的子树
这种方法与后序遍历有相同的时间复杂度.
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class Test:
    def __init__(self):
        self.maxSum = -2 ** 31

    def findMaxSubTree(self, root, maxRoot):
        if root == None:
            return 0

        lmax = self.findMaxSubTree(root.lchild, maxRoot)
        rmax = self.findMaxSubTree(root.rchild, maxRoot)

        sums = lmax + rmax + root.data

        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.data = root.data
        return sums

    def constructTree(self):
        root = BiTNode()
        node1 = BiTNode()
        node2 = BiTNode()
        node3 = BiTNode()
        node4 = BiTNode()
        root.data = 6
        node1.data = 3
        node2.data = -7
        node3.data = -1
        node4.data = 9
        root.lchild = node1
        root.rchild = node2

        node1.lchild = node3
        node1.rchild = node4
        return root


if __name__ == '__main__':
    # 构造二叉树
    test = Test()
    root = test.constructTree()
    maxRoot = BiTNode()
    test.findMaxSubTree(root, maxRoot)
    print('最大紫薯和:', test.maxSum)
    print('对应的子树根节点为:', maxRoot.data)
