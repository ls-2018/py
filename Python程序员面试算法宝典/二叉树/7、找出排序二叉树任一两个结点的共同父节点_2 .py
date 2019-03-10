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
import math


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


class IntRef:
    def __init__(self):
        self.num = None


def getNo(root, node, number):
    """
    找出结点在二叉树中的编号
    :param root:
    :param node: 待查找的结点
    :param number: 在二叉树中的编号
    :return:
    """
    if root == None:
        return False
    if root == node:
        return True
    tmp = number.num
    number.num = 2 * tmp

    # node结点在root的左子树中,左子树的编号为当前节点的2倍
    if getNo(root.lchild, node, number):
        return True
    # node 结点在root的右子树中,右子树编号为当前结点的2倍加1
    else:
        number.num = tmp * 2 + 1
        return getNo(root.rchild, node, number)


def getNodeFromNum(root, number):
    """
    根据结点的编号找到对应的结点
    :param root:
    :param number:  结点的编号
    :return:
    """
    if root == None or number < 0:
        return None
    if number == 1:
        return root
    # 结点编号对应二进制的位数(最高位一定为1,因为根节点代表1 )
    lens = int((math.log(number) / math.log(2)))
    # 去掉根节点表示的1
    number -= (1 << lens)
    while lens > 0:
        # 如果这一位二进制的值为1
        # 那么编号为number的结点必定在当前结点的右子树上
        if 1 << (lens - 1) & number == 1:
            root = root.rchild
        else:
            root = root.lchild
        lens -= 1
    return root


def FindParentNode(root, node1, node2):
    ref1 = IntRef()
    ref1.num = 1
    ref2 = IntRef()
    ref2.num = 1
    getNo(root, node1, ref1)
    getNo(root, node2, ref2)
    num1 = ref1.num
    num2 = ref2.num
    # 找出公共的父结点
    while num1 != num2:
        if num1 > num2:
            num1 //= 2
        else:
            num2 //= 2
    # num1 就是最近的公共父结点的编号,通过节点编号找到对应的结点
    return getNodeFromNum(root, num1)


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(arr, 0, len(arr) - 1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.rchild

    res = FindParentNode(root, node1, node2)
    if res != None:
        print(node1.data, node2.data, '最近的公共父结点为：', res.data)
    else:
        print('没有公共父结点')

# 7、找出排序二叉树任一两个结点的共同父节点_2
