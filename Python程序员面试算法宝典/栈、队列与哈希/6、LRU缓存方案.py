'''
最近最少使用

缓存一定量的数据，当超过设定的阈值时就把一些过期的数据删掉。

1、使用双向链表实现的队列，队列的最大容量为缓存的大小。在使用过程中，把最近使用的页面移动到队列头，最近没有使用的页面将被放在队列尾的位置。
2、使用一个哈希表，把页号作为键，把缓存在队列中的结点的地址作为值
当引用一个页面时，如果所需的页面在内存中，只需要把这个页对应的结点移动到队列的前面。
如果所需的页面不在内存中，此时需要把这个页面加载到内存中。简单地说，就是将一个新结点添加到队列的前面，并在哈希表中更新相应的节点地址。
如果队列是满的，那就从队尾部一处一个结点，并将新节点添加到队列的前面。
'''

'''为什么用双向链表，以删除最后一个节点为例，我们要怎么删除最后一个？逆向的获取相对正向来说的倒数第二个，将其正向下一个结点删除'''

from collections import deque


class LRU:
    def __init__(self, cachesize):
        self.cacheSize = cachesize
        self.queue = deque()
        self.hashSet = set()

    # 判断缓存队列是否已满
    def isQueueFull(self):
        return len(self.queue) == self.cacheSize

    # 把页号为pageNum的页缓存到队列中，同时也添加到hash表中
    def enqueue(self, pageNum):
        # 如果队列满了，需要删除对位的缓存的项
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        # 把新缓存的结点同时添加到hash表中
        self.hashSet.add(pageNum)

    """
    当访问某一个page的时候，会调用这个函数，对于访问的page有两种情况：
        1、如果page在缓存队列中，直接把这个节点移动到对首
        2、如果page不在缓存队列中，把这个page缓存到对首
    """

    def accessPage(self, pageNum):
        # page不在缓存队列中，把它缓存到对首
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        # page 已经在缓存队列中了，移动到队首
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


if __name__ == '__main__':
    # 假设缓存大小为3
    lru = LRU(3)

    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)

    lru.printQueue()