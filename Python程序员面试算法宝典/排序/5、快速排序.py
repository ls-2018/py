"""
快速排序是一种非常搞笑的排序算法,它采用    分而治之    的思想,把大的拆分为小的,把小的拆分为更小的.



原理:
    对于一组给定的记录,通过一趟排序后,将原序列分为两部分,其中前部分的所有记录均比后部分的记录小,
        然后在一次对前后两部分的记录进行快速排序
步骤:
1、分解,将输入的序列[m,...,n]划分为两个非空子序列[m,...,k] 和 [k+1,...,n];使得左序列中任何一元素都比右边小
2、递归求解:递归调用快速排序算法分别对[m,...,k] 和 [k+1,...,n]进行排序
3、合并:由于对分解出的两个子序列的排序是就地进行的,所以在所有递归都完成后,  数组就已经排好序



   最坏时间复杂度为O(N*N)       区间的左边或右边为空,而另一边的区间中的记录项仅比排序前少了一项,
                                    即选取的基准关键字是待排序的所有记录中最小或者最大的
   最好时间复杂度为O(n*logn)    每次区间划分的结果都是基准关键字左右两边的序列长度相等或者相差为1,
                                    即选择的基准关键字为待排序的记录的中间值
   平均的时间复杂度为O(nlogn)    是一种稳定的排序方法,空间复杂度为O(1)


    空间复杂度:快排过程中需要一个栈空间来实现递归.
        当每次对区间的划分都比较均匀时,递归树的最大深度为logn取整+1
        当每次都使得有一边的序列长度为0,递归树的深度为n,
        在每轮排序结束后比较基准关键字左右的记录个数,对记录多的一边先进行排序,此时栈的最大深度可降为logn
        因此平均空间复杂度为logn


    关键子的选取:
        默认选择数组中第一个元素

        1、将首\尾\中间位置上的元素进行比较,将中值作为关键字,与首交换
        2、在这个数组中，随机选取一个作为关键字，与首交换

"""


def find_mid(lists, left, right):
    """选取合适的关键字"""
    key1 = lists[left]
    key2 = lists[right]
    key3 = lists[(left + right) // 2]
    maxNo = max(key1, key2, key3)
    minNo = min(key1, key2, key3)
    key = [key2, key1, key3]
    key.remove(maxNo)
    key.remove(minNo)
    key = key[0]
    if key == key1:
        pass
    elif key == key2:
        lists[left], left[right] = left[right], left[left]
    else:
        lists[left], lists[(left + right) // 2] = key, lists[left]
    return key


def quick_sort(lists, left, right):
    # 快速排序
    if left > right:
        return lists

    key = find_mid(lists, left, right)

    low = left
    high = right

    while left < right:  # 遍历一次将开始元素放到应该放的位置,左小右大
        while left < right and lists[right] >= key:
            right -= 1  # 退出条件,lists[right] 小于key,
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1  # 退出条件,lists[left] 大于等于key,
        lists[right] = lists[left]

    # 最后left 与right相等
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    # lists = [5, 4, 3, 2, 1]
    print('排序前序列为:', lists)
    quick_sort(lists, 0, len(lists) - 1)
    print('排序后序列为:', lists)
