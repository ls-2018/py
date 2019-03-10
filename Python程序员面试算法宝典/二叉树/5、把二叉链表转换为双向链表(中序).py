"""

转换后的双向链表中结点的顺序与二叉树的中序遍历的顺序相同,因此,可以对二叉树的中序遍历算法进行修改,
                            通过在中序遍历的过程中修改结点的指向来转换成一个排序的双向链表.

在求解的时候需要特别注意递归的约束条件以及边界情况,例如双向链表为空的时候

"""


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class Test:
    def __init__(self):
        self.pHead = None  # 双向链表的头指针
        self.pEnd = None  # 双向链表的尾指针

    def arraytotree(self, arr, start, end):
        root = None
        if end >= start:
            root = BiTNode()
            mid = (start + end + 1) // 2
            # 树的根节点为数组中间的元素
            root.data = arr[mid]
            # 递归的用左半部分数据构造root的左子树
            root.lchild = self.arraytotree(arr, start, mid - 1)
            # 递归的用右半部分数组构造root的右子树
            root.rchild = self.arraytotree(arr, mid + 1, end)
        else:
            root = None
        return root

    def inOrderBSTree(self, root):
        if root == None:
            return
        # 转换root的左子树
        self.inOrderBSTree(root.lchild)

        root.lchild = self.pEnd  # 使当前结点的左孩子指向双向链表中的最后一个结点
        if self.pEnd == None:
            self.pHead = root  # 双向列表为空,当前遍历的结点为双向链表的头结点
        else:
            self.pEnd.rchild = root  # 使双向链表中最后一个结点的右孩子指向当前结点

        self.pEnd = root  # 将当前结点设为双向链表中最后一个结点

        # 转换root的右子树
        self.inOrderBSTree(root.rchild)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    test = Test()
    root = test.arraytotree(arr, 0, len(arr) - 1)
    test.inOrderBSTree(root)

    print('转换后双向链表正向遍历')
    cur = test.pHead
    while cur != None:
        print(cur.data)
        cur = cur.rchild

    print('转换后双向链表逆向遍历')
    cur = test.pEnd
    while cur != None:
        print(cur.data)
        cur = cur.lchild
#