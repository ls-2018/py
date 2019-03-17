"""
归并排序是利用递归与分治技术将数据序列划分成为越来越小的半子表,再对半子表排序,最后再用递归步骤将排序号的半子表合并成为越来越大的有序序列



原理:
    对于给定的一组记录,首先将每两个相邻的长度为1的子序列进行归并,得到n/2个长度为2 或1的有序子序列,再将其两两归并,反复执行此过程,直到得到一个有序序列为止


二路归并排序的过程需要进行logn 次.每一趟归并排序的操作,就是将两个有序子序列进行归并,而每一对有序子序列归并时,
    记录的比较次数均小于等于记录的移动次数,记录移动的排序次数均等于文件中记录的个数n,即每一堂趟并的时间时间复杂度为O(N)

    最好\最坏\平均 的时间复杂度为O(nlogn)    是一种稳定的排序方法,空间复杂度为O(1)



Stable 与 Not Stable 的比较
    稳定排序算法会将相等的元素值维持其相对次序。
    如果一个排序算法是稳定的，当有两个有相等的元素值 R 和 S，且在原本的列表中 R 出现在 S 之前，那么在排序过的列表中 R 也将会是在 S 之前。
"""


def merge(left, right):
    """将两个有序数列,按照从小到大组合起来"""
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        result += right[j:]
    if j == len(right):
        result += left[i:]
    return result


def merge_sort(lists):
    #
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == '__main__':
    print(merge_sort([3, 4, 2, 8, 9, 5, 1]))
