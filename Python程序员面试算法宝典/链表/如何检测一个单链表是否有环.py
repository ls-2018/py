'''
只可能是在尾部有环
方法一:
    单独有一个列表,存放已访问过的,新来的都去列表里看有没有

方法二:
    快慢指针,速度 fast = 2 * slow
    当fast=slow判断为有环,fast.next为空无环

引申:
    如果有环,怎么判断环的入口在哪?
    假设fast走了2s步,--->slow走了s步

    2s = s + n*r ;r为环长
    设整个链表长L,入口环与相遇点路径长度为x(绕了好几圈),起点到环入口点的距离为a,
    ---->
        s = n * r
        s = a + x = n * r
        a + x =(n-1)*r +r = (n-1)*r + L - a
        a = (n-1)*r + (L - a -x)
        起点              相遇点
    ---->
        于是在链表头和相遇点,分别设一个指针,每次各走一步,两个指针相遇,且相遇点第一个点为环入口点
        期间走了n-1个环长
'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


# 构造链表
def constructList():
    i = 0
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    # 构造链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None

        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = head.next.next.next  # 建环
    return head

def isLoop(head):
    if head  == None or head.next ==None:
        return
    # 初始slow与fast都指向链表第一个结点
    slow = head.next
    fast = head.next
    while fast!=None and fast.next !=None:
        slow=slow.next
        fast = fast.next.next
        if slow ==fast:
            return slow
        return None


def findLoopNode(head,meetNode):
    first = head.next
    second = meetNode
    while first!=second:
        first=first.next
        second = second.next
    return first


if __name__ == '__main__':
    head = constructList()

    meetNode = isLoop(head)
    loopNode = None
    if meetNode!=None:
        print('有环')
        loopNode= findLoopNode(head,meetNode)
        print('环的入口为',loopNode.data)
    else:
        print('无环')