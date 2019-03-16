"""
给定一个词典 和两个相同长度的开始和目标单词,
找到从  开始到目标的最小链的长度,
要求链中相邻元素只有一个字符不同
"""
from collections import deque


# 用来存储单词链的队列
class QItem:
    def __init__(self, word, lens):
        self.word = word
        self.lens = lens


# 判断两个字符串是否只有一个不同的字符串
def isAdjacent(a, b):
    diff = 0
    if len(a) != len(b):
        return False
    lens = len(a)
    i = 0
    while i < lens:
        if list(a)[i] != list(b)[i]:
            diff += 1
        if diff > 1:
            return False
        i += 1
    return diff == 1


# 返回从start到target的最短链
def shortestChainLen(start, target, D):
    Q = deque()
    item = QItem(start, 1)
    Q.append(item)  # 把第一个字符串添加进来
    while len(Q) > 0:
        curr = Q[0]
        Q.pop()
        for it in D:
            temp = it
            # 如果这两个字符串只有一个字符不同
            if isAdjacent(curr.word, temp):
                item.word = temp
                item.lens = curr.lens + 1
                Q.append(item)  # 把这个字符串放入到队列中
                # 把这个字符串从队列中删除来避免被重复遍历
                D.remove(temp)
                # 通过转变后得到了目标字符
                if temp == target:
                    return item.lens
    return 0


if __name__ == '__main__':
    D = ['pooN', 'pbcc', 'zamc', 'poIc', 'pbca', 'pbIc', 'poIN', ]
    start = 'TooN'
    target = 'pbca'
    print('最短的链条的长度为:', shortestChainLen(start, target, D))
