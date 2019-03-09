'''
1、把push序列依次入栈,直到栈顶元素等于pop序列的第一个元素,然后栈顶元素出栈,pop序列移动到第二个元素
2、如果栈顶元素继续等于pop序列现在的元素,则继续出栈并pop后移,否则对push序列继续入栈
3、如果push序列已经全部入栈,但是pop序列未全部遍历,而且栈顶元素不等于当前pop元素,那么这个序列不是一个可能的出栈序列.如果栈为空,而且pop序列也全部被遍历,则说明这是一个可能的pop序列
'''


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


def isPopSerial(push, pop):
    if push == None or pop == None:
        return False
    pushLen = len(push)
    popLen = len(pop)
    if pushLen != popLen:
        return False
    pushIndex = 0
    popIndex = 0
    stack = Stack()
    while pushIndex < pushLen:
        # 把push序列依次入栈,直到栈顶元素等于pop序列的第一个元素
        stack.push(push[pushIndex])
        pushIndex += 1
        # 栈顶元素出栈,pop序列移动到下一个元素
        while (not stack.empty()) and stack.peek() == pop[popIndex]:
            stack.pop()
            popIndex += 1
    # 栈为空,且pop序列中元素都被遍历过
    return stack.empty() and popIndex == popLen


if __name__ == '__main__':
    push = '12345'
    pop = '32541'
    if isPopSerial(push, pop):
        print(pop, '是', push, '的出栈组合')
    else:
        print(pop, '不是', push, '的出栈组合')
