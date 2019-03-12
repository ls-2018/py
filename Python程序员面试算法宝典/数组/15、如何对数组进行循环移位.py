"""
把一个含有N个元素的数组循环右移K位，要求时间复杂度O(N），且只能使用两个附近变量
abcd1234----->1234abcd


需要考虑一下K与N的关系            K = K%N15、如何对数组进行循环移位

# 上面是移动KN次, ---->弄一个K%N的数组，存储数据，然后直接向后移动K%N个数。
"""


def rightShift(arr, k):
    if arr is None:
        print('参数不合法')
        return
    lens = len(arr)
    k %= lens
    while k != 0:
        tmp = arr[lens - 1]
        i = lens - 1
        while i > 0:
            arr[i] = arr[i - 1]
            i -= 1
        arr[0] = tmp
        k -= 1


# 翻转法
def reverse(arr, start, end):
    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1


def rightShift_2(arr, k):
    if arr is None:
        print('参数不合法')
        return
    lens = len(arr)
    k %= lens
    reverse(arr, 0, lens - k - 1)
    reverse(arr, lens - k, lens - 1)
    reverse(arr, 0, lens - 1)


if __name__ == '__main__':
    k = 4
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    rightShift(array, k)
    print(array)
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    rightShift_2(array, 5)
    print(array)
