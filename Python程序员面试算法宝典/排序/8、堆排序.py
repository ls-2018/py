"""
堆一般分为大根堆、小根堆两种。
对于给定n个记录的序列（r1,r2,r3....rn) 当且仅当满足条件ri >= r(2i）i=1,2,3..n 时称之为大根堆，此时堆顶元素必为最大值。
对于给定n个记录的序列（r1,r2,r3....rn) 当且仅当满足条件ri <= r(2i）i=1,2,3..n 时称之为小根堆，此时堆顶元素必为最小值。




堆排序的思想是对于给定的n个元素，初始时把这些元素看做一颗顺序存储的二叉树，然后将其调整为一个大根堆，然后将堆的最后一个与堆顶元素(即二叉树的根节点）进行交换后，堆的最后一个
元素即为最大元祖，接着将前n-1个元素（不包括最大值）重新调整为一个大根堆，再讲堆顶元素与当前堆的最后一个元素进行交换后得到次大
的元素，重复该过程直到调整的堆中只剩一个元素时为止， 该元素即为最小元素，此时可得到一个有序序列

堆排序主要包括两个过程 ：
    1、构建堆
    2、交换堆顶元素与最后一个元素的位置
"""


def adjust_heap(lists, i, size):
    # 从0开始
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxs = i
    if i < size // 2:
        if lchild < size and lists[lchild] > lists[maxs]:
            maxs = lchild
        if rchild < size and lists[rchild] > lists[maxs]:
            maxs = rchild
        if maxs != i:
            lists[maxs], lists[i] = lists[i], lists[maxs]
            adjust_heap(lists, maxs, size)


def build_heap(lists, size):
    for i in range(0, size // 2)[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('排序前的序列为：', lists)
    heap_sort(lists)
    print('排序后的序列为：', lists)
"""
堆排序方法对元素较少的文件效果一般，但是对于元素较多的文件还是很有效的，其运行时间主要耗费在创建堆和反复调整堆上，
堆即使在最坏的情况下，其时间复杂度也为O(nlog),它是一种不稳定的排序方法
"""