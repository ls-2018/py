"""
为了实现对二叉树的层序遍历,就要求在遍历一个结点的同时记录下它的孩子结点的信息,然后按照这个记录的顺序来访问结点的数据,在实现的时候可以采用队列来存储当前遍历到的结点的孩子结点,从而实现二叉树的层序遍历.

"""
from collections import deque


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


# 方法一:队列
def printTreeLayer(root):
    if root == None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data)

        if p.lchild != None:
            queue.append(p.lchild)
        if p.rchild != None:
            queue.append(p.rchild)

#
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(arr, 0, len(arr) - 1)
    print('层序遍历结果为:')
    printTreeLayer(root)
