def bubble_sort(lists):
    print('排序前:', lists)
    n = len(lists)
    for i in range(n):
        for j in range(i + 1, n):
            if lists[i] > lists[j]: # 保证每次循环中,都可以使最小数跑到首位
                lists[i], lists[j] = lists[j], lists[i]
                print('排序中:', lists)    #
    print('排序后:', lists)


if __name__ == '__main__':
    bubble_sort([3, 4, 2, 8, 9, 5, 1])
