"""
中位数就是一组数据从小到大排序后中间的那个数字.
如果长度为偶数,那么中位数的值就是中间两个数相加除2
如果长度为奇数,那么中位数的值就是中间的那个数字
"""

"""
快速排序:每一次局部递归后,都能保证一变小于等于;另一边大于

分治思想:仅仅是一边?



1、首先转换为求一列数中第i小的数
1、求中位数，就是求第（length/2+1)小的数




当第一次使用类快速排序后，分割元素的下标为pos
    1、当pos>length/2时，说明中位数在数组左半部分，那么继续在左半部分查找
    2、当pos=length/2时，说明找到该中位数，返回A[pos]即可
    3、当pos<length/2时，说明中位数在数组右半部分，那么继续在数组右半部分查找
以上默认是奇数长度
"""


class Test:
    def __init__(self):
        self.pos = 0

    # 以array[low]为基准把数组分成两部分
    def partition(self, array, low, high):
        key = array[low]
        while low < high:
            while low < high and array[high] > key:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] < key:
                low += 1
            array[high] = array[low]
        array[low] = key
        self.pos = low

    def get_mid(self, array):
        low = 0
        n = len(array)
        high = n - 1
        mid = (low + high) // 2
        while 1:
            #
            self.partition(array, low, high)
            if self.pos == mid:
                break
            elif self.pos > mid:
                high = self.pos - 1
            else:
                low = self.pos + 1

        return array[mid] if (n % 2) != 0 else (array[mid] + array[mid + 1]) / 2


if __name__ == '__main__':
    arr = [7, 5, 3, 1, 11, 9]
    print(Test().get_mid(arr))

"""
为什么使用类，
内部需要的参数不用通过（×××）传递
外部需要的参数也不需要return

"""
