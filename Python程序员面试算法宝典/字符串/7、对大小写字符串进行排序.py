"""
假设有一个大小写字母都有的字符串
排序结果:  小写在前面,大写字母在后面
思路:类似快速排序的方法处理,可以用两个索引分别指向字符串的首和尾,首索引正向遍历找到第一个大写字母,尾索引逆向遍历字符串,找到第一个小写字母,
    两个索引位置的字符交换,然后两个两个索引沿着相应的方向继续移动,重复上述操作,直到首索引大于或等于尾索引为止
"""


def reverse(array):
    lens = len(array)
    begin = 0
    end = lens - 1
    while begin < end:
        # 正向遍历找到第一个大写字母
        while end > begin:
            if 'A' <= array[begin] <= 'Z':
                break
            begin += 1
        # 反向遍历找到第一个小写字母
        while end > begin:
            if 'a' <= array[end] <= 'z':
                break
            end -= 1
        temp = array[begin]
        array[begin] = array[end]
        array[end] = temp


if __name__ == '__main__':
    arr = list('AbcDrfFXCZXVDDdFG')
    reverse(arr)
    print(arr)
# 7、对大小写字符串进行排序
