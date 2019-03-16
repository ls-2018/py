"""
分配一个分区时，从头开始看此案容量是否够，标记   p[J]
    待下一次分区时，先从标记的处开始，在从头开始
举例：
    磁盘为[120,120,120],分区为[60,60,80,20,80]可分配,如果为[20,80,80,20,80]则分配失败
"""


def is_allocable(d, p):
    dIndex = 0  # 磁盘分区下标
    i = 0
    while i < len(p):
        # 找到符合条件的磁盘
        while dIndex < len(d) and p[i] > d[dIndex]:
            dIndex += 1
        # 没有可用的磁盘
        if dIndex >= len(d):
            return False
        # 给磁盘分区
        d[dIndex] -= p[i]
        i += 1
    return True


if __name__ == '__main__':
    d = [120, 120, 120]
    p = [60, 60, 80, 20, 80]
    if is_allocable(d, p):
        print('分配成功')
    else:
        print('失败')