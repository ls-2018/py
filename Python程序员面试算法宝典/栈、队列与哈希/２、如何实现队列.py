'''
功能：入队、出队、查看队首元素、查看队列大小

'''

# 数组实现
'''
front   记录队列首元素
rear    记录队列尾元素往后的一个位置
入队列时只需要将待入队的元素放到元素下表为rear的位置,同时执行rear+,出队列的时候只需要执行front+即可

缺点：出队列后数组前半部分的空间不能被充分利用,解决这个问题的方法是把数组看成一个环状的空间（循环队列）,当数组最后一个被占用后,
    可以从数组首位置开始循环利用.而这样也就限制了数组的大小.

'''


class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0  # 队列头
        self.rear = 0  # 队列尾

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    # 获取队首元素
    def getFront(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]

    # 获取队列尾元素
    def getBack(self):
        if self.isEmpty():
            return None
        return self.arr[self.rear - 1]

    # 删除队列首元素
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print('队列已经为空')

    def enQueue(self, item):
        self.arr.append(item)
        self.rear += 1

    def __enter__(self):
        print(123)

    def __exit__(self, *arg, **kwargs):
        print(arg, kwargs)  # (None, None, None) {}


with MyQueue() as f:
    pass

if __name__ == '__main__':
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print('队列首元素为：', queue.getFront())
    print('队列尾元素为：', queue.getBack())
    print('队列大小为：', queue.size())
