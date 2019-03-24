"""
有20个数组，每个数组有500各元素，并且是有序排列好的，如何在20*500个数中找出排名前500的数

思路：假设是降序排列

1、首先建立大根堆，堆的大小为数组的个数20，把每个数字最大的值（数组第一个）存放到堆中。python中heapq是小根堆，通过输入和输出的元素分别 取相反数来实现大根堆的功能

2、接着删除堆顶元素，保存到另外一个大小为500的数组中，然后向大根堆堆顶插入删除的元素所在数组的下一个元素。

3、重复12步骤，直至删除个数为最大的k个数

"""
import heapq


def getTop(data):
    rowSize = len(data)
    columnSize = len(data[0])
    result3 = [None] * columnSize
    # 保持一个最小堆，这个堆存放来自20个数组的最小数
    heap = []
    i = 0
    while i < rowSize:
        arr = (None, None, None)  # 数组设置三个变量，分别为数值，数值来源的数组，数值在数组中的次序index
        arr = (-data[i][0], i, 0)
        heapq.heappush(heap, arr)
        i += 1
    num = 0
    while num < columnSize:
        # 删除堆顶元素
        d = heapq.heappop(heap)
        result3[num] = -d[0]
        num += 1
        if num >= columnSize:
            break
        # 将value 置为该数原数组里的下一个数
        arr = (-data[d[1]][d[2] + 1], d[1], d[2] + 1,)
        heapq.heappush(heap, arr)
    return result3


if __name__ == '__main__':
    data = [
        [29, 17, 14, 2, 1],
        [19, 17, 16, 15, 6],
        [30, 25, 20, 14, 5]
    ]
    print(getTop(data))
