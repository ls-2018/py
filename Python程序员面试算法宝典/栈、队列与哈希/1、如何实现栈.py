'''
实现一个栈的数据结构，使其具有以下方法：压栈、弹栈、取栈顶元素、判断栈是否为空以及或取栈中元素的个数。
# 使用数组实现
    把数组的首元素当做栈底，同时记录栈中元素个数size，设数组首地址为arr，
# 使用链表实现

'''


class MyStack:
    # 模拟栈
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            print('栈已经为空')
            return None

    def push(self,item):
        self.items.append(item)

if __name__ == '__main__':
    s=MyStack()
    s.push(4)
    print('栈顶元素为：',s.top())
    print('栈的大小：',s.size())
    s.pop()
    print('出栈成功')
    s.pop()