"""
寻找一条从左上角arr[0][0]到右下角arr[m-1][n-1]的路线，使得沿途经过的数组中的整数的和最小
只能右移  或向下走

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


# 动态规划
def getMinPath_2(arr):
    if arr is None or len(arr) == 0:
        return 0
    row = len(arr)
    col = len(arr[0])
    # 用来保存计算的中间值
    cache = [[0] * col for i in range(row)]
    cache[0][0] = arr[0][0]
    # 第一行和第一列的走法是固定的
    i = 1
    while i < row:
        cache[i][0] = cache[i - 1][0] + arr[i][0]
        i += 1
    j = 1
    while j < col:
        cache[0][j] = cache[0][j - 1] + arr[0][j]
        j += 1
    # 遍历二维数组的过程中不断吧计算结果保存到cachezh
    print('路径为：')
    i = 1
    while i < row:
        j = 1
        while j < col:
            # print(cache[i-1][j],cache[i][j-1])
            # 可以确定选择路线为arr[i][j-1]
            if cache[i - 1][j] > cache[i][j - 1]:  # 上边和走边进行比较
                cache[i][j] = cache[i][j - 1] + arr[i][j]
                print("[", i, ',', j - 1, ']', )
            else:
                cache[i][j] = cache[i - 1][j] + arr[i][j]
                print("[", i - 1, ',', j, ']', )
            j += 1
        i += 1
    print("[", row - 1, ',', col - 1, ']', )
    print('最小值为：', cache[row - 1][col - 1])


def getMinPath(arr):
    if arr == None or len(arr) == 0:
        return 0
    # return getMinPath_1(arr, len(arr) - 1, len(arr[0]) - 1)
    return getMinPath_2(arr)


if __name__ == '__main__':
    arr = [
        [1, 4, 3],
        [8, 7, 5],
        [2, 1, 5]
    ]
    print(getMinPath(arr))
