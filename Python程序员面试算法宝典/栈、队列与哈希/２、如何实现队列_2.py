'''
链表实现
'''


class LNode():
    def __init__(self, x):
        self.data = x
        self.next = None


class MyQueue:
    # 分配头结点
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    # 判断队列是否为空,如果为空返回true,否则返回false
    def empty(self):
        if self.pHead == None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.pHead
        while p != None:
            p = p.next
            size += 1
        return size

    # 入队列,把元素加到队尾
    def enQueue(self, item):
        p = LNode(item)
        if self.pHead == None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p

    # 出队列,删除队首元素
    def deQueue(self):
        if self.pHead == None:
            print('出队列失败,队列已经为空')
        self.pHead = self.pHead.next
        if self.pHead == None:
            self.pEnd = None

    def getFront(self):
        if self.pHead == None:
            print('获取队列首元素失败,队列已经为空')
            return None
        return self.pHead.data

    def getBack(self):
        if self.pEnd == None:
            print('获取队列尾元素失败,队列已经为空')
            return None
        return self.pEnd.data


if __name__ == '__main__':
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print('队列首元素为：', queue.getFront())
    print('队列尾元素为：', queue.getBack())
    print('队列大小为：', queue.size())
