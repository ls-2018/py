"""
有m台机器，有n个任务，每台机器执行时间耗费不同，求最短时间，以及任务分布情况


每一个任务都与判断分给哪一个机器执行合适

"""


def calculate_process_time(t, n):
    """

    :param t: 每个服务器处理的时间
    :param n: 任务个数
    :return: 各个服务器执行完任务所需的时间
    """
    if t is None or n <= 0:
        return None
    m = len(t)
    proTime = [0] * m
    i = 1
    while i <= n:
        minTime = proTime[0] + t[0]  # 把任务给第j个机器后这个机器的执行时间
        minIndex = 0
        j = 1  # 从第二个进行比较,如果是0 ,则会与自身比较一次
        while j < m:
            # 分配到第j台机器上后执行时间更短
            if minTime > proTime[j] + t[j]:  # 最短时间  与   已经分配任务的时间+此任务需要的时间    两者相比较
                minTime = proTime[j] + t[j]
                minIndex = j
            j += 1
        proTime[minIndex] += t[minIndex]
        i += 1
    return proTime


if __name__ == '__main__':
    t = [7, 10]
    n = 6
    proTime = calculate_process_time(t, n)
    if proTime:
        total_time = proTime[0]
        i = 0
        while i < len(proTime):
            print('第', i + 1, '台服务器有', proTime[i] / t[i], '个任务执行总时间为：', proTime[i])

            if proTime[i] > total_time:
                total_time = proTime[i]
            i += 1
        print('任务执行总时间为:', total_time)
