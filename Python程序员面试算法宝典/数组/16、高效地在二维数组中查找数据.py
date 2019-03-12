"""
一个M*N二维数组：
从左到右依次增大，每一列从上到下依次增大。

"""


def findWithBinary(array, data):
    if array is None:
        return False

    # 从二维数组右上角元素开始遍历
    i = 0
    rows = len(array)
    columns = len(array[0])
    j = columns - 1
    while i < rows and j >= 0:
        demo = array[i][j]
        # 在数组中找到data，返回
        if array[i][j] == data:
            return True
        # 当前遍历到数组中的值大于data，data肯定不在这一列中
        elif array[i][j] > data:
            j -= 1
        # 当前遍历到数组中的值小于data，data肯定不在这一行中
        elif array[i][j] < data:
            i += 1
        print(demo)
    return False


if __name__ == '__main__':
    array = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [40, 41, 42, 43, 55]
    ]
    print(findWithBinary(array, 9))
    print(findWithBinary(array, 42))
