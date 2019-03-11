# 方法一
"""max  和 min 两个变量；一共比较  2n-2次"""

# 分治法
"""
以下是 奇数 偶数 分治

还有将其分为左右两半分治
"""


class MaxMin:
    def __init__(self):
        self.max = None
        self.min = None

    def getMax(self):
        return self.max

    def getMin(self):
        return self.min

    def GetmaxAndmin(self, arr):
        if arr is None:
            print('参数不合法')
            return
        i = 0
        lens = len(arr)
        self.max = arr[0]
        self.min = arr[0]
        # 两两分组，把较小的数放在左半部分，较大的数放到右半部分
        i = 0
        while i < (lens - 1):
            if arr[i] < arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
            i += 2
        # 在各个分组的左半部分找最小值
        i = 2
        while i < lens:
            if arr[i] > self.max:
                self.max = arr[i]
            i += 2
        # 如果数组中元素的个数是奇数个，最后一个元素备份在一起，需要做特殊处理
        if lens % 2 == 1:
            if self.max < arr[lens - 1]:
                self.max = arr[lens - 1]

            if self.min > arr[lens - 1]:
                self.min = arr[lens - 1]


if __name__ == '__main__':
    array = [7, 3, 19, 40, 4, 7, 1]
    m = MaxMin()
    m.GetmaxAndmin(array)
    print('max:', m.getMax())
    print('min:', m.getMin())
