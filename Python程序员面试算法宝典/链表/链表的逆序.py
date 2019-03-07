class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None

    '''
    给定一个带头结点的单链表,将其逆序
    head->1->2->3->4->5->6->7
    head->7->6->5->4->3->2->1
    '''


# 就地逆序
def Reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    pre = None  # 前驱结点
    cur = None  # 当前结点
    next = None  # 后继结点
    # 把链表首结点变为尾结点
    cur = head.next
    next = cur.next
    cur.next = None

    pre = cur
    cur = next
    # # 使用当前遍历到的结点cur指向其前驱结点
    # while cur.next != None:
    #     next = cur.next
    #     cur.next = pre
    #     pre = cur
    #     cur = cur.next
    #     cur = next
    # # 链表最后一个结点指向倒数第二个结点
    # cur.next = pre
    # # 链表的头结点指向原来的尾结点
    # head.next = cur


def InsertReverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    cur = None  # 当前结点
    next = None  # 后继结点
    # 把链表首结点变为尾结点
    cur = head.next.next
    # 设置链表第一个结点为尾结点
    head.next.next = None
    # 把遍历到结点插入到头结点的后面
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


if __name__ == '__main__':
    i = 1
    # 链表首结点
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1


    cur = head.next
    print('逆序前:', end='')
    while cur != None:
        print('->', cur.data, end='', sep='')
        cur = cur.next
    print()

    InsertReverse(head)


    cur = head.next
    print('逆序后:', end='')
    while cur != None:
        print('->', cur.data, end='', sep='')
        cur = cur.next
    print()

# 我更喜欢InsertReverse这种方法.
