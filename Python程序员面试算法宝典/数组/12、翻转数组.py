def rotate_arr(array):
    lens = len(array)
    # 打印二维数组右上半部分
    i = lens - 1
    while i > 0:
        row = 0
        col = i
        while col < lens:
            print(array[row][col], end=' ')
            row += 1
            col += 1
        print()
        i -= 1

    # 打印二维数组左下半部分
    i = 0
    while i < lens:
        row = i
        col = 0
        while row < lens:
            print(array[row][col], end=' ')
            row += 1
            col += 1
        print()
        i += 1


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_arr(arr)
