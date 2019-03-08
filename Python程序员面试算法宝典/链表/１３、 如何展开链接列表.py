'''
3 -> 5 -> 9 -> 223
|    |    |
4    6    14
     7

3 4 5 6 7 9 14 223


使用归并排序的合并操作,简而言之把这些链表来逐个归并。
具体而言，可以使用递归的方法，递归地合并已经扁平化的链表与当前的链表。在实现的过程中可以使用ｄｏｗｎ指针来存储扁平化处理后的链表
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class MergeList:
    def __init__(self):
        self.head = None
        # 合并后的有序的链表

    def merge(self, a, b):
        # 如果其中一个为空，直接返回另外一个链表
        if a == None:
            return b
        if b == None:
            return a
        if a.data < b.data:
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)

        return result

    def flatten(self, root):
        if root == None or root.right == None:
            return root
        root.right = self.flatten(root.right)
        root = self.merge(root, root.right)
        return root

    def insert(self, head_ref, data):
        new_node = Node(data)
        new_node.down = head_ref
        head_ref = new_node
        return head_ref

    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end=',')
            tmp = tmp.down


if __name__ == '__main__':
    L = MergeList()
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)
    L.head = L.flatten(L.head)
    L.printList()
