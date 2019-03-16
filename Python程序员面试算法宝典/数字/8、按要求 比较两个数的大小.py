"""
不能使用大于、小于以及if语句


max
|a-b| == a-b

if a>b:
    abs(a-b) = a-b
elif a<b:
    abs(a-b) = b-a
else
    abs(a-b) = 0

"""


def maxs(a, b):
    return int(((a + b) + abs(a - b)) / 2)


if __name__ == '__main__':
    print(maxs(3, 7 + 4))
