class MyXOR:
    def __init__(self):
        self.BITS = 32

    def xor(self, x, y):
        res = 0
        i = self.BITS - 1
        while i >= 0:
            # 获取x与y当前的bit值
            b1 = (x & (1 << i)) > 0
            b2 = (y & (1 << i)) > 0

            # 只有这两位都是1 或0的时候结果为0
            if b1 == b2:
                flag = 0
            else:
                flag = 1
            res <<= 1
            res |= flag
            i -= 1
        return res

    def xor_2(self, x, y):
        return (x | y) & (~x | ~y)


if __name__ == '__main__':
    print(MyXOR().xor(3, 5))  # 11 101
    print(MyXOR().xor_2(3, 5))  # 11 101
    print(3 ^ 5)

"""
^   为1 有2种情况        
|   为1 有3种情况
&   为1 有1种情况

---->    ~|   &  |    就是2种重叠的

"""
