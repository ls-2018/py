# 哈希法
# 这个算法有问题，排序的结果不准


def sort(arr):
    data_count = dict()
    n = len(arr)
    # 把数组放到map中
    i = 0
    while i < n:
        if str(arr[i]) in data_count:
            data_count[str(arr[i])] += 1
        else:
            data_count[str(arr[i])] = 1
        i += 1
    index = 0
    for k, v in data_count.items():
        i = v
        while i > 0:
            arr[index] = k
            index += 1
            i -= 1


if __name__ == '__main__':
    arr = [15, 12, 15, 2, 2, 12, 2, 3, 12, 100, 3, 3]
    sort(arr)
    print(arr)
