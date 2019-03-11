"""
数组[3,4,5,1,2]为数组 [1,2,3,4,5]的一个旋转，该数组的最小值为1.

特点：先递增，突然下降到最小值，再递增
注意：
    -   数组本身是没有发生过旋转的
    -   全部相等
    -   大部分都相等
"""

"""
按照二分查找的思想,给定数组arr，首先定义两个变量low和high，分别表示数组的第一个元素和最后一个元素的下标。
    顶一个元素应该是大于或者等于最后一个元素的（当旋转个数为0，即没有旋转的时候，要单独处理，直接返回数组第一个元素）。
接着遍历数组中间的元素arr[mid],其中mid=（high+low）/2

1、如果arr[mid] < arr[mid-1],则arr[mid]一定是最小值
2、如果arr[mid + 1] < arr[mid],则arr[mid + 1]一定是最小值
3、如果arr[high] > arr[mid],则最小值一定在数组左半部分
4、如果arr[mid] > arr[low],则最小值一定在数组右半部分
5、如果arr[mid] == arr[low]且arr[mid] > arr[high]则此时无法区分最小值是在数组的左半部分还是右半部分。这种情况下，只能分别
    在数组的左右两半部分找最小值minL和minR，再从中求出最小值
"""


def getMin_1(arr, low, high):
    # 如果旋转个数为0，即没有旋转，单独处理，直接返回数组头元素
    if high < low:
        return arr[0]

    # 只剩下一个元素一定是最小值
    if high == low:
        return arr[low]

    # mid = (low+high)/2 采用下面写法防止溢出
    mid = low + ((high - low) >> 2)
    # 判断是否arr[mid]为最小值
    if arr[mid] < arr[mid - 1]:
        return arr[mid]
    # 判断是否arr[mid+1]为最小值
    elif arr[mid + 1] < arr[mid]:
        return arr[mid + 1]
    # 最小值一定在数组左半部分
    elif arr[high] > arr[mid]:
        return getMin_1(arr, low, mid - 1)
    # 最小值一定在数组右半部分
    elif arr[mid] > arr[low]:
        return getMin_1(arr, mid + 1, high)
    # arr[low] == arr[mid] && arr[high] == arr[mid]
    # 这种情况下无法确定最小值所在的位置，需要在左右两部分分别进行查找
    else:
        return min(getMin_1(arr, low, mid - 1), getMin_1(arr, mid + 1, high))


def getMin(arr):
    if arr is None:
        print('参数不合法')
        return
    else:
        return getMin_1(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    array = [5, 6, 1, 2, 3, 4]
    mins = getMin(array)
    print(mins)
    array2 = [1, 1, 0, 1]
    mins = getMin(array2)
    print(mins)
