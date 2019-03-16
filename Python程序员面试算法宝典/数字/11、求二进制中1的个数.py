# 移位法
def countOne(n):
    count = 0
    while n > 0:
        if (n & 1) == 1:  # 最后一位是否为1
            count += 1
        n >>= 1
    return count


if __name__ == '__main__':
    print(countOne(9))
