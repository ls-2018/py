"""
对二叉树进行左右反转
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
    node2.data = 7
    node3.data = 1
    node4.data = x
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    return root


def reverseTree(root):
    if root is None:
        return None

    reverseTree(root.lchild)
    reverseTree(root.rchild)
    root.rchild, root.lchild = root.lchild, root.rchild


from collections import deque


def printTree(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data, end='->', )
        if p.lchild is not None:
            queue.append(p.lchild)
        if p.rchild is not None:
            queue.append(p.rchild)
    print()


if __name__ == '__main__':
    root = constructTree(2)
    printTree(root)
    reverseTree(root)
    printTree(root)
