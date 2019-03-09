"""
如果要把一个有序的整数数组放到二叉树中,那么所构造出来的二叉树必定也是一颗有序的二叉树

实现思路:
    去数组的中间元素作为根结点,将数组分成左右两部分,对数组的两部分用递归的方法分别构建左右子树了.
"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


#
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


def printTreeMidOrder(root):
    if root == None:
        return
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data)
    if root.rchild != None:
        printTreeMidOrder(root.rchild)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('数组')
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1
    root = arraytotree(arr, 0, len(arr) - 1)
    print('转换成树的中序遍历为')
    printTreeMidOrder(root)
    print()
