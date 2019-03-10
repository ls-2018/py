"""
两颗二叉树相等是指这颗二叉树有着相同的结构,并且在相同位置上的结点有相同的值.
中序判读:
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def isEqual(root1, root2):
    if root1 and root2:
        if root1.data != root2.data:
            return False
        return isEqual(root1.lchild, root2.lchild) and isEqual(root1.rchild, root2.rchild)
    if root1 == root2 == None:
        return True
    return False


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
    root2 = constructTree(1)
    equal = isEqual(root1, root2)
    if equal:
        print('=')
    else:
        print('!=')
