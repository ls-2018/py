"""
有一个升序序列的数组,求该数组中绝对值最小的数
[-10,-5,-2,7,15,50]
"""
# 方法一:顺序比较    abs(), O(N)
# 方法二:二分法
"""
1、数组第一个数为非负数,那么第一个它就是
2、数组第一个数为非正数,那么最后一个它就是
3、有正有负
    找到分界点,如果为0,它就是
    比较分界点左右两边的数,来确定
"""


def findMin(array):
    if array is None or len(array) <= 0:
        print('参数不合理')
        return
    lens = len(array)
    # 数组中没有负数
    if array[0] >= 0:
        return array[0]
    # 数组中没有正数
    if array[-1] <= 0:
        return array[-1]

    mid = 0
    begin = 0
    end = lens - 1
    absMin = 0
    # 数组中既有正数又有负数
    while True:
        mid = begin + (end - begin) // 2
        # 如果等于0,肯定是绝对值最小
        if array[mid] == 0:
            return 0
        elif array[mid] > 0:
            if array[mid - 1] > 0:
                end = mid - 1
            elif array[mid - 1] == 0:
                return 0
            else:  # 找到正负数的分界点
                break
        else:
            if array[mid + 1] < 0:
                begin = mid + 1
            elif array[mid + 1] == 0:
                return 0
            else:  # 找到正负数的分界点
                break

    # 判断分界点左右两边的绝对值
    if array[mid] > 0:
        if array[mid] < abs(array[mid - 1]):
            absMin = array[mid]
        else:
            absMin = array[mid - 1]
    else:
        if abs(array[mid]) < array[mid + 1]:
            absMin = array[mid]
        else:
            absMin = array[mid + 1]
    return absMin


if __name__ == '__main__':
    array = [-10, -5, -2, 7, 15, 50]
    print('绝对值最小的数为:', findMin(array))
