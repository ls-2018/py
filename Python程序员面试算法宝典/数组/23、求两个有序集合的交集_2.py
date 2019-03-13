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


def getIntersection2(l1, l2):
    result = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        s1 = l1[i]
        s2 = l2[j]
        if s1.getMin() < s2.getMin():
            if s1.getMax() < s2.getMin():
                i += 1
            elif s1.getMax() < s2.getMax():
                result.append(MySet(s2.getMin(), s1.getMax()))
                i += 1
            else:
                result.append(MySet(s2.getMin(), s2.getMax()))
                j += 1
        elif s1.getMin() <= s2.getMax():
            if s1.getMax() <= s2.getMax():
                result.append(MySet(s1.getMin(), s1.getMax()))
                i += 1
            else:
                result.append(MySet(s1.getMin(), s2.getMax()))
                j += 1
        else:
            j += 1
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
