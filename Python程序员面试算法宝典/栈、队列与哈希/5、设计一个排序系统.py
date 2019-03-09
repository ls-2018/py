"""
设计一个排序系统,能够让每个进入队伍的用户都能看到自己在队伍中所处的位置和变化,队伍可能随时有人加入和退出;
                当有人退出影响到用户的位置排名时需要及时反馈到用户.

不仅要实现队列常见的入队列和出队列的功能,而且还要实现队列中任意一个元素都可以随时出队列,且出队列后需要更新队列用户位置的变化.
"""
from collections import deque

"""
deque.popleft()
deque.pop()
deque.append()
deque.appendleft()
deque.remove()
"""


class User:
    def __init__(self, id, name):
        self.id = id  # 唯一标识的用户
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSeq(self):
        return self.seq

    def setSeq(self, seq):
        self.seq = seq

    def getId(self):
        return self.id

    def equals(self, obj):
        return self.id == obj.getId()

    def toString(self):
        return 'id:' + str(self.id) + '    name:' + self.name + '         seq:' + str(self.seq)


class MyQueue:
    def __init__(self):
        self.q = deque()

    def enQueue(self, u):  # 进入队列尾部
        u.setSeq(len(self.q) + 1)
        self.q.append(u)

    # 对头出队列
    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    # 出队列后更新队列中每个人的序列
    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    def printList(self):
        for u in self.q:
            print(u.toString())

    def deQueuemove(self, u):
        self.q.remove(u)
        self.updateSeq()


if __name__ == '__main__':
    u1 = User(1, 'user1')
    u2 = User(2, 'user2')
    u3 = User(3, 'user3')
    u4 = User(4, 'user4')

    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.deQueue()  # 队首元素u1出队列
    queue.deQueuemove(u3)  # 队列中间的元素u3出队列
    queue.printList()
