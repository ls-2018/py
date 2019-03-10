"""
方法二：
    在构造二叉树的时候，为结点编号(按照完全二叉树)

    假设根节点为1 （二进制）

    左孩子--->向左移一位，末尾补0
    右孩子--->向左移一位，末尾补1

    根据孩子的编号与父结点的关系：    孩子//2 = 父结点
    这样就可以很简单的找出来了

    那么, 重点在于构造构造二叉树了
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

