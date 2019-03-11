"""
给定一个二叉树，求各个路径的最大和，路径可以以任何结点作为起点和终点。
            2
          5    3
最大和的路径为结点 5->2->3，这条路径的和为10，因此返回10
"""
"""
思路：

1、求出以root.left为起始节点，叶子结点为终结点的最大路径和为maxLeft
2、同理求出以root.right为起始结点，叶子结点为终结点的最大路径和maxRight。
    leftMax = root.val + maxLeft    # 左子树最大路径和可能为负
    rightMax = root.val + maxRight  # 右子树最大路径和可能为负
    allMax = root.val + rightMax + leftMax # 左右子树的最大路径和都不为负
    
    因此，包含root结点的最大路径和为tmpMax = max(rightMax,leftMax,allMax)
    
    在求出包含root结点的最大路径后，如果tmpMax>max,那么更新最大路径和为tmpMax。

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class IntRef:
    def __init__(self):
        self.val = None


def max(a, b, c):
    """
    求a,b,c的最大值
    :param a:
    :param b:
    :param c:
    :return:
    """
    maxs = a if a > b else b

    maxs = maxs if maxs > c else c

    return maxs


def findMaxPathRecursive(root, maxs):
    """
    寻找最长路径
    :param root:
    :param maxs:
    :return:
    """
    if root is None:
        return 0
    else:
        # 求左子树以root.left为起始结点的最大路径和
        sumLeft = findMaxPathRecursive(root.left, maxs)
        # 求右子树以root.right为起始结点的最大路径和
        sumRight = findMaxPathRecursive(root.right, maxs)
        # 求以root为起始结点，叶子结点为结束结点的最大路径和
        allMax = root.val + sumLeft + sumRight
        leftMax = root.val + sumLeft
        rightMax = root.val + sumRight
        tmpMax = max(leftMax, rightMax, allMax)
        if tmpMax > maxs.val:
            maxs.val = tmpMax
        subMax = sumLeft if sumLeft > sumRight else sumRight
        # 返回以root为起始结点，叶子结点为结束结点的最大路径和
        return root.val + subMax


def findMaxPath(root):
    maxs = IntRef()
    maxs.val = 0
    findMaxPathRecursive(root, maxs)

    return maxs.val


if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(3)
    right = TreeNode(5)
    root.left = left
    root.right = right
    print(findMaxPath(root))
