"""
一个数列，每一个元素  都能被 2 3 5 整除，1,是第一个  求第1500个值是多少
"""


# 蛮力
def search(n):
    i = 0
    count = 1
    i = 2
    while count != n:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            count += 1
        i += 1
    return i


# 数字规律法
def search_2(n):
    array = []
    i = 1
    while i <= 2 * 3 * 5:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            array.append(i)
        i += 1
    print(array)  # [2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
    # 符合条件的都是上边数组元素的倍数
    lens = len(array)

    # 排除1,因为1不在上面的数组内
    return ((n - 1) // lens) * 30 + array[n % lens - 1]


if __name__ == '__main__':
    print(search_2(1500))
