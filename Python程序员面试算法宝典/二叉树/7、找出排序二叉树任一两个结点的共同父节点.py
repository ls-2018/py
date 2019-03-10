"""
方法一：
    如果知道从根节点到当前结点的路径
        6->3->2->1
        6->3->5
        那么 5,2 的共同父结点就是    3,6

缺点：
    在获取路径时，最复杂的情况时间复杂度为O(n)，而且需要多次
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class MyStack:
    def __init__(self):
        self.items = []

    # 判断stack是否为空，如果为空返回true，否则返回false
    def empty(self):
        return len(self.items) == 0

    # 获取栈中元素的个数
    def size(self):
        return len(self.items)

    # 入栈：把e放到栈顶
    def push(self, e):
        self.items.append(e)

    # 出栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    # 返回栈顶元素
    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None


def getPathFromRoot(root, node: BiTNode(), s: MyStack()):
    """
    获取二叉树从根节点到node结点的路径
    :param root:
    :param node: 二叉树中某个结点
    :param s: 用来存储路径的栈
    :return:
    """
    if root == None:
        return False
    if root == node:
        s.push(root)  # push 的 每一个node父结点
        return True
    if getPathFromRoot(root.lchild, node, s) or getPathFromRoot(root.rchild, node, s):
        # 判断是否在左孩子、右孩子
        s.push(root)  # push 的根节点
        return True
    return False


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
    stack1 = MyStack()
    stack2 = MyStack()

    getPathFromRoot(root, node1, stack1)
    getPathFromRoot(root, node2, stack2)

    commonParent = None

    while stack1.peek() == stack2.peek():
        commonParent = stack1.peek()  # 就找第一个
        stack1.pop()
        stack2.pop()
    return commonParent


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(arr, 0, len(arr) - 1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.lchild
    res = FindParentNode(root, node1, node2)
    if res != None:
        print(node1.data, node2.data, '最近的公共父结点为：', res.data)
    else:
        print('没有公共父结点')
#
