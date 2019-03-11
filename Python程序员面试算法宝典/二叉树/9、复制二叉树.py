"""
对于给定一个二叉树根节点，复制该树，返回新建树的根节点
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def createDupTree(root):
    if root is None:
        return None

    dupTree = BiTNode()
    dupTree.data = root.data
    dupTree.lchild = createDupTree(root.lchild)
    dupTree.rchild = createDupTree(root.rchild)
    return dupTree


def printTreeMidOrder(root):
    if root == None:
        return
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data)
    if root.rchild != None:
        printTreeMidOrder(root.rchild)


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


if __name__ == '__main__':
    root1 = constructTree(1)
    root2 = createDupTree(root1)
    print('原始二叉树中序遍历：')
    printTreeMidOrder(root1)
    print('新的二叉树中序遍历')
    printTreeMidOrder(root2)
