"""
有两个有序的集合,集合中的么个元素都是一段范围,求其交集
{[4,8],[9,13]}这就是有序
"""


class MySet:
    def __init__(self, mins, maxs):
        self.mins = mins
        self.maxs = maxs

    def getMin(self):
        return self.mins

    def getMax(self):
        return self.maxs

    def setMin(self, mins):
        self.mins = mins

    def setMax(self, maxs):
        self.maxs = maxs


def getINtersection(s1: MySet, s2: MySet):
    if s1.getMin() < s2.getMin():
        if s1.getMax() < s2.getMin():
            return None
        elif s1.getMax() <= s2.getMax():
            return MySet(s2.getMin(), s1.getMax())
        else:
            return MySet(s2.getMin(), s2.getMax())
    elif s1.getMin() <= s2.getMax():
        if s1.getMax() <= s2.getMax():
            return MySet(s1.getMin(), s1.getMax())
        else:
            return MySet(s1.getMin(), s2.getMax())
    else:
        return None


def getIntersection2(l1, l2):
    result = []
    i = 0
    while i < len(l1):
        j = 0
        while j < len(l2):
            s = getINtersection(l1[i], l2[j])
            if s is not None:
                result.append(s)
            j += 1
        i += 1
    return result


if __name__ == '__main__':
    l1 = []
    l2 = []
    l1.append(MySet(4, 8))
    l1.append(MySet(9, 13))
    l2.append(MySet(6, 12))
    result = getIntersection2(l1, l2)
    i = 0
    while i < len(result):
        print(result[i].getMin(), '      ', result[i].getMax())
        i += 1

"""
没有利用到序列有序的条件
"""
