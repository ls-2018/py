"""
已知３个升序整数数组　　a[l],b[m],c[n],请在三个数组中各找出一个元素,使得组成的三元组距离最小。

Ｄistance = max(|a[i]-b[j]|,|a[i]-c[k]|,|b[j]-c[k]|)

"""
"""
# 方法１：
    三次循环Ｏ（n^3),找出所有的情况进行比较
# 方法２：
    最小距离法
    假设当前三个元素分别为ai, bi, ci,且ai <= bi <= ci;此时距离肯定为ci-ai
        1、  如果接下来求ai, bi, c(i+1)的距离,由于c(i+1)>=ci,因此最小距离仍为ci-ai
        
        2、  如果接下来求ai, b(i+1), ci的距离,由于b(i+1)>=bi,
                如果b(i+1)<=ci,距离仍为ci-ai；
                如果b(i+1)>ci,距离为b(i+1)-ai；,显然比ci-ai大,因此最小距离仍为ci-ai
        3、  如果接下来求a(i+1), bi, ci的距离,此时它们的距离显然小于ci-ai
        因此只需要考虑第三种情况
"""


def mins(a, b, c):
    """
    获取三个数中的最小值
    :return:
    """
    mins = a if a < b else b
    mins = mins if mins < c else c
    return mins


def maxs(a, b, c):
    """获取三个数中的最大值"""
    maxs = b if a < b else a
    maxs = c if maxs < c else maxs
    return maxs


def minDistance(a, b, c):
    aLen = len(a)
    bLen = len(b)
    cLen = len(c)
    minDist = 2 ** 32

    i = 0  # 数组a 的下标
    j = 0  # 数组b 的下标
    k = 0  # 数组c 的下标

    while True:
        curDist = maxs(abs(a[i] - b[j]), abs(a[i] - c[k]), abs(b[j] - c[k]))
        if curDist < minDist:
            minDist = curDist
        # 找出当前遍历到三个数组的最小值
        minsd = mins(a[i], b[j], c[k])
        if minsd == a[i]:
            i += 1
            if i >= aLen:
                break
        elif minsd == b[j]:
            j += 1
            if j >= bLen:
                break
        else:
            k += 1
            if k >= cLen:
                break
    return minDist


if __name__ == '__main__':
    a = [3, 4, 5, 7, 15]
    b = [10, 12, 14, 16, 17]
    c = [20, 21, 23, 24, 27, 30]
    print('最小的距离为:', minDistance(a, b, c))
