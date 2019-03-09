"""
最简单的就是四重遍历，，但是时间复杂度是N^4

字典法：
    以数对为单位进行遍历，在遍历过程中，把数对和数对的值存储在字典中（键为数对的和，值为数对），当遍历到下一个键值对时，如果它的和在字典中已经存在，那么久找到了满足条件的键值对。

"""


# 用来存储数对
class pair:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second


def findPairs(arr):
    # 键为数对的和，值为数对
    sumPair = dict()
    n = len(arr)
    # 遍历数组中所有可能的数对
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            # 如果这个数对的和在map中没有，则放入map中
            sums = arr[i] + arr[j]
            if sums not in sumPair:
                sumPair[sums] = pair(i, j)
            # map中已经存在与sum相同的数对了，找出并打印出来
            else:
                # 找出已经遍历过的并存储在map中和为sum的数对
                p = sumPair[sums]
                print(str(arr[p.first]), ',', str(arr[p.second]), '    ', str(arr[i]), ',', str(arr[j]))
                return True
            j += 1
        i += 1


if __name__ == '__main__':
    arr = [3, 4, 7, 10, 20, 9, 8]
    findPairs(arr)

# 就是两次遍历，  i+j:(i,j)的数据格式存储,只要有i+j相同的就打印
