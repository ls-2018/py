'''
采用从头插入新节点的方法，最好使用带头结点的链表，这样可以保证对每个节点的操作都是相同的。

入栈：从头插入
出栈：队尾弹出
'''

class LNode():
    def __new__(self,x):
        self.data =x
        self.next =None

class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    # 判断stack是否为空，如果为空返回true，否则返回false
    def empty(self):
        if self.next==None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.next
        while p!=None:
            p=p.next
            size+=1
        return size

    # 入栈：把e放到栈顶
    def push(self,e):
        p = LNode
        p.data=e
        p.next=self.next
        self.next=p
    # 出栈
    def pop(self):
        tmp=self.next
        if tmp!=None:
            self.next=tmp.next
            return tmp.data
        print('栈已经为空')
        return None
    # 获取栈顶元素
    def top(self):
        if self.next!=None:
            return self.next.next
        print("栈已经为空")
        return None
if __name__ == '__main__':
    s=MyStack()
    s.push(4)
    print('栈顶元素为：',s.top())
    print('栈的大小：',s.size())
    s.pop()
    print('出栈成功')
    s.pop()