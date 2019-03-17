"""
100个灯泡排成一排;
第一轮     都打开
第二轮     2 4 , ... 100 关灯
第三轮     3 6 9     99    开着的关掉,关着的打开

求第100轮结束的时候,还有几盏灯亮着

"""


def factorIsOdd(a):
    total = 0
    i = 1
    while i < a:
        if a % i == 0:
            total += 1
        i += 1
    if total % 2 == 1:
        return 1
    else:
        return 0


def totalCount(num, n):
    count = 0
    i = 0
    while i < n:
        if factorIsOdd(num[i]) == 1:
            print(num[i])
            count += 1
        i += 1
    return count


def func_1(n):
    demo = [True] * n
    i = 2
    while i <= n:
        j = i
        while j <= n:
            if j % i == 0:
                demo[j - 1] = not demo[j - 1]
            j += 1
        i += 1
    count = 0
    for k, v in enumerate(demo):
        if v:
            count += 1
            print(k + 1)
    print(count)


if __name__ == '__main__':
    func_1(100)  # 一层一层遍历,遍历100次
    print('------------------')
    print(totalCount([i for i in range(100)], 100))  # 一个元素,经历100次的的变化,在观察最后的结果
