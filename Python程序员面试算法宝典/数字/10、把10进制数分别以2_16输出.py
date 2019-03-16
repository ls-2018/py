def intToBinary(n):
    hexNum = 8 * 8  # 二进制的位数(long  占8个字节）
    bit = []
    for i in range(hexNum):
        b = n >> i
        c, d = divmod(b, 2)  # 商和余数
        bit.append(str(d))
    return ''.join(bit[::-1])


def intToHex(s):
    hexs = ''
    while s != 0:
        a, b = divmod(s, 16)

        if b < 10:
            hexs = str(b + int('0')) + hexs
        else:
            hexs = hexs + chr(b - 10 + ord('A'))

        s = a
    return hexs


if __name__ == '__main__':
    print('10的2进制输出为:', intToBinary(10))
    print('10的16进制输出为:', intToHex(140))
