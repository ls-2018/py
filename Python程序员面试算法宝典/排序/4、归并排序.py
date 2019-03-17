"""
归并排序是利用递归与分治技术将数据序列划分成为越来越小的半子表,再对半子表排序,最后再用递归步骤将排序号的半子表合并成为越来越大的有序序列



原理:
    对于给定的一组记录,首先将每两个相邻的长度为1的子序列进行归并,得到n/2个长度为2 或1的有序子序列,再将其两两归并,反复执行此过程,直到得到一个有序序列为止

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
