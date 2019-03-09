"""
A  入队
B  出队



如果栈B不为空,则直接弹出栈B的数据
如果栈B为空,则依次弹出栈A的数据,放入栈B中,在弹出栈B的数据.

"""


class Stack:
    # 模拟栈
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print('栈已经为空')
            return None

    # 压栈
    def push(self, item):
        self.items.append(item)


class MyStack:
    def __init__(self):
        self.A = Stack()  # 入栈
        self.B = Stack()  # 出栈

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.empty():
            while not self.A.empty():
                self.B.push(self.A.peek())
                self.A.pop()
        first = self.B.peek()
        self.B.pop()
        return first


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print('队列首元素为:', stack.pop())
    print('队列首元素为:', stack.pop())
