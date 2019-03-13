# 方法一：
"""
AVL树，根据数组中的数构建一个AVL树，这里需要对AVL树做适当的扩展，在节点中增加一个额外的数据域来记录这个数字出现的次数，在AVL树构建完成后，可以对AVL树
进行中序遍历，根据每个结点对应数字出现的次数，把遍历结果放回到数组中就完成了排序
时间复杂度O(nlogM/log2)
空间复杂度O(n)
"""


class Node:
    # AVL树结点    自平衡二叉查找树。在AVL树中任何节点的两个子树的高度最大差别为1
    def __init__(self, data):
        self.left = self.right = None
        self.height = self.count = 1


class Sort:
    # 中序遍历AVL树，把遍历结果放入到数组中
    def inorder(self, arr, root, index):
        if root is not None:
            # 中序遍历左子树
            index = self.inorder(arr, root.left, index)
            # 把root结点对应的数字根据出现的次数放入到数组中
            i = 0
            while i < root.count:
                arr[index] = root.data
                index += 1
                i += 1
            # 中序遍历右子树
            index = self.inorder(arr, root.right, index)
        return index

    def getHeight(self, node):
        """得到树的高度"""
        if node is None:
            return 0
        else:
            return node.height

    def rightRotate(self, y):
        # 把以y为根的左子树向右旋转
        x = y.left
        T2 = x.right
        # 旋转
        x.right = y
        y.left = T2
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        # 返回新的根节点
        return x

    def leftRotate(self, x):
        # 把以x为根的左子树向左旋转
        y = x.right
        T2 = x.left
        # 旋转
        y.left = x
        y.right = T2
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1

        # 返回新的根节点
        return y

    def getBalance(self, N):
        # 获取新的平衡因子
        if N is None:
            return 0
        return self.getHeight(N.left) - self.getHeight(N.right)

    def insert(self, root, data):
        """
        如果data在AVL树中不存在，则把data插入到AVL树中，否则把这个结点对应的count+1即可
        """
        if root is None:
            return Node(data)
        # data在树中存在，把对应的结点的count+1
        if data == root.data:
            root.count += 1
            return root
        # 在左子树中继续查找data是否存在
        if data < root.data:
            root.left = self.insert(root.left, data)
        # 在右子树中继续查找data是否存在
        else:
            root.right = self.insert(root.right, data)

        # 插入新的结点后更新root结点的高度
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        # 获取树的平衡因子
        balance = self.getBalance(root)
        # 如果树不平衡，根据四种情况进行调整
        # LL
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        # RR
        elif balance < -1 and data > root.left.data:
            return self.leftRotate(root)
        # LR
        elif balance > 1 and data > root.left.data:
            return self.rightRotate(root)
        # RL
        elif balance < -1 and data < root.right.data:
            root.height = self.rightRotate(root.height)
        # 返回树的根节点
        return root

    # 使用AVL树实现排序
    def sort(self, arr):
        root = None
        n = len(arr)
        i = 0
        while i < n:
            root = self.insert(root, arr[i])
            i += 1
        index = 0
        self.inorder(arr, root, index)


if __name__ == '__main__':
    arr = [15, 12, 15, 2, 2, 12, 2, 3, 12, 100, 3, 3]
    s = Sort()
    s.sort(arr)
    print(arr)
