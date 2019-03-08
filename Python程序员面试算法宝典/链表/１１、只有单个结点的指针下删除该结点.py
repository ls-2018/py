'''
１、如果这个结点是链表的最后一个结点,那么无法删除这个结点
２、如果这个结点不是链表的最后一个结点,可一通过把其后继结点的数据复制到当前结点中，然后删除后继结点的方法来实现。

'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


def Print(flag, head):
    demo = ''
    if flag == 0:
        demo = '逆序前:'
    elif flag == 1:
        demo = '      '
    elif flag == 2:
        demo = '逆序后:'
    cur = head.next
    print(demo, end='')
    while cur != None:
        print('->', cur.data, end='', sep='')
        cur = cur.next
    print()


# 构造链表
def constructList():
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    p = None
    # 构造链表
    while i < 7:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        if i == 5:
            p = tmp
        cur.next = tmp
        cur = tmp
        i += 1
    return head,p


def RemoveNode(p):
    if p == None or p.next == None:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True


if __name__ == '__main__':
    head, p = constructList()
    Print(0, head)
    result = RemoveNode(p)
    if result:
        Print(2, head)
