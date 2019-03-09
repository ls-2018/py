"""
在算法设计中,经常会采用空间换取时间的方式来提高时间复杂度,也就是说,采用额外的存储空间来降低操作的时间复杂度.
具体而言,在实现的时候使用两个栈结构,一个栈用来存储数据,另外一个栈用来存储栈的最小元素.

实现思路:如果当前入栈的元素比原来栈中的原来栈中的最小值还小,则把这个值压入保存最小元素的栈中;
    在出栈的时候,如果当前出栈的元素恰好为当前栈中的最小值,保存最小值的栈顶元素也出栈,使得当前最小值变为当前最小值入栈之前的那个最小值.
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
        self.elemStack = Stack()  # 用来存储栈中元素
        self.minStack = Stack()  # 栈顶永远存储当前elemStack中最小的值

    def push(self, item):
        """遇到一个问题,当push的是倒序,minStack的大小会很大"""
        self.elemStack.push(item)
        # 更新保存最小元素的栈
        if self.minStack.empty():
            self.minStack.push(item)
        else:
            if item <= self.minStack.peek():
                self.minStack.push(item)

    def pop(self):
        topData = self.elemStack.peek()
        self.elemStack.pop()
        if topData == self.mins():
            self.minStack.pop()
        return topData

    def mins(self):
        if self.minStack.empty():
            return 2 ** 32
        else:
            return self.minStack.peek()


if __name__ == '__main__':
    stack = MyStack()
    stack.push(5)
    print(stack.mins())
    stack.push(4)
    print(stack.mins())
    stack.push(4)
    print(stack.mins())
    stack.pop()
    print(stack.mins())
