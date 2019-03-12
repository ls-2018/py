"""
方法一 两次遍历  n *n
"""


# 方法二重复利用已经计算的子数组和
def max_sub_array(array):
    if array is None or len(array) < 1:
        print('输入不合法')
        return
    max_sum = array[0]  # 设置初始值
    i = 0
    while i < len(array):
        sums = 0
        j = i
        while j < len(array):
            # Sum[i,j] = Sum[i,j-1] + array[j]
            sums += array[j]

            if sums > max_sum:
                max_sum = sums
            j += 1
        i += 1
    return max_sum


# 动态规划
def max_sub_array_2(array):
    """# 牛逼
    假设数组最后的一个元素array[n-1]与最大子数组的关系
    1、最大子数组包含array[n-1],即最大子数组以array[n-1]结尾
    2、array[n-1]单独构成最大子数组
    3、最大子数组不包含array[n-1],那么求array[1...n-1]最大子数组,转换为求array[1...n-2]
    All[n-1]=max(End[n-1],array[n-1],All[n-2])
    """
    if array is None or len(array) < 1:
        print('输入不合法')
        return
    n = len(array)
    End = [None] * n
    All = [None] * n
    End[n - 1] = array[n - 1]
    All[n - 1] = array[n - 1]
    # End[0] = All[0] = array[0]
    # i = 1
    # while i < n:
    #     End[i] = max(End[i - 1] + array[i], array[i])  # array[0...i]中包含array[i]的最大子数组和
    #
    #     All[i] = max(End[i - 1] + array[i], array[i], All[i - 1])  # array[1...i]的最大子数组和
    #     i += 1
    # return All[n - 1]
    # 优化一下
    End = All = array[0]
    i = 1
    while i < n:
        All = max(End + array[i], array[i], All)  # array[1...i]的最大子数组和
        End = max(End + array[i], array[i])  # array[0...i]中包含array[i]的最大子数组和
        i += 1
    return All


if __name__ == '__main__':
    arr = [1, -2, 4, 8, -4, 7, -1, -5]
    print('连续最大和:', max_sub_array(arr))
    print('连续最大和:', max_sub_array_2(arr))
