"""
# 方法一：
    先排序（快排），再根据坐标取[k-1]的值
# 方法二：
    遍历K次，得到K次遍历所得到的最小值，在比较

    也可以采用堆排序
#　方法三：
    类快速排序方法
    快速排序的基本思想为：将数组array[low...high]中某一个元素作为划分依据，然后把数组划分为三部分
                所有的元素的值小于等于array[i],array[i],所有元素都大于array[i]


    思路：
        １、如果i-low == k-1,说明array是第Ｋ小的元素，那么就直接返回array[i]
        ２、如果i-low>k-1,说明第Ｋ小的元素肯定在array[low...i-1]中,那么只需要递归地在array[low...i-1]中找到第Ｋ小的元素即可　。
        ３、如果i-low<k-1,说明第Ｋ小的元素肯定在array[i+1,high]中，那么只需要递归地在array[i+1...high]中找到第k-(i-low)-1小的元素即可
            对于数组（４，０，１，０，２，３）,第一次划分后，划分为下面三部分
            （３，０，１，０，２），（４），（）
            　（２，０，１，０）（３）（）
               （０，０，１）（２）（）
                （０）（０）（１）
            此时，i=1,low=0,(i-1=1)<(k-1=2),接下来需要在（１）中找第k-(i-low)-1=1小的元素即可
"""


def findSmallK(array, low, high, k):
    """找出数组中第Ｋ小的元素"""
    i = low
    j = high
    splitElem = array[low]
    # 把小于等于splitElem的数放到数组中splitElem的左边，大于的放到右面
    while i < j:
        while i < j and array[j] >= splitElem:
            j -= 1
        if i < j:
            array[i] = array[j]
            i += 1
        while i < j and array[i] <= splitElem:
            i += 1
        if i < j:
            array[j] = array[i]
            j -= 1
        array[i] = splitElem
        # spiltElem在子数组array[low~high]中下标的偏移量
        subArrayIndex = i - low
        # splitElem在array[low~high]所在的位置恰好为k-1，那么他就是第Ｋ小的元素
        if subArrayIndex == k - 1:
            return array[i]
        elif subArrayIndex > k - 1:
            return findSmallK(array, low, i - 1, k)
    else:
        return findSmallK(array, i + 1, high, k - (i - low) - 1)


if __name__ == '__main__':
    k = 3
    array = [4, 0, 1, 0, 2, 3]
    print('第', k, '小的值为：', findSmallK(array, 0, len(array) - 1, k))
