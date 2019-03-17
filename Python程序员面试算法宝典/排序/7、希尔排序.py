"""
希尔排序也称为  缩小增量排序

基本原理:   首先将待排序的元素分成多个自诩列,使得每个子序列的元素个数相对较少,对各个子序列分别进行直接插入排序
            待整个待排序序列   '基本有序后'  在对所有元素进行一次直接插入排序



具体步骤:
    1、选择一个步长序列 t1,t2,t3 ... ,tk  满足ti > tj (i<j )  tk=1
    2、按照步长序列个数k,对待排序序列进行k次排序
    3、每次排序,根据对应的步长ti,将待排序序列分割成成ti个子序列 (序号%ti取余),分别对各个子序列进行直接插入排序

    当步长为1 时,所有元素作为一个序列来处理,



希尔排序的关键并不是随便地分组后各自排序,而是将像个某个  增量 的记录组成一个子序列,实现跳跃式移动,使得排序的效率提高.
希尔排序是一种不稳定的排序方法,平均时间复杂度  为O(nlogn)
最差时间复杂度O(N^S)(1<S<2)

空间复杂度为O(1)
"""


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group = group // step
    return lists


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    print(shell_sort(lists))
