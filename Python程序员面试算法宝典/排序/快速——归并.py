"""
单单就代码而言:快速排序 比归并排序,多了一步排序

相同点:都是基于分治思想,即首先把待排序的元素分为两组,然后分别对这两组排序,最后在合并起来

不同点:进行的分组策略不同,后面的合并策略也不同.

    归并排序的分组策略:是假设待排序的元素存放在数组中,那么把数组前面一半作为一组,后面一半作为另外一组.

    快速排序则是根据元素的值来分组,即大于某个值的元素放在一组,小于某个值的放在另外一组,该值称之为基准值.
        所以对于快排来说,基准值的选取很重要,(决定了分组的状况)

    总体来说,如果分组策略越简单,那么后面的合并策略就越复杂,
        因为快排在分组时,已经根据元素大小来分组了,而合并的时候,只需要把两个分组合并起来就行了,
        归并排序则需要对两个有序的数组根据大小进行合并

"""
