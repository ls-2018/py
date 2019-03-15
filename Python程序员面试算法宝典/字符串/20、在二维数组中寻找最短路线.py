"""
寻找一条从左上角arr[0][0]到右下角arr[m-1][n-1]的路线，使得沿途经过的数组中的整数的和最小


f(i,j) = min(f(i-1,j),f(i,j-1)) + arr[i][j]
"""


# 递归
def getMinPath_1(arr, i, j):
    # 倒着走到了第一个结点，递归结束
    if i == 0 and j == 0:
        return arr[i][j]
    # 选取两条可能路径上的最小值
    elif i > 0 and j > 0:
        return arr[i][j] + min(getMinPath_1(arr, i - 1, j), getMinPath_1(arr, i, j - 1))

    # 下面两个条件只可以选择一个
    elif i > 0 and j == 0:
        return arr[i][j] + getMinPath_1(arr, i - 1, j)
    elif j > 0 and i == 0:
        return arr[i][j] + getMinPath_1(arr, i, j - 1)


def getMinPath(arr):
    if arr == None or len(arr) == 0:
        return 0
    return getMinPath_1(arr, len(arr) - 1, len(arr[0]) - 1)


if __name__ == '__main__':
    arr = [
        [1, 4, 3],
        [8, 7, 5],
        [2, 1, 5]
    ]
    print(getMinPath(arr))
