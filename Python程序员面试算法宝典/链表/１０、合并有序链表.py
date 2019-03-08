'''
合并有序链表
逆序前:->1->3->5
逆序前:->2->4->6
逆序后:->1->2->3->4->5->6
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
def constructList(start):
    i = start
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    # 构造链表
    while i < 7:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 2
    return head


# 　合并链表
def Merge(head1, head2):
    if head1 == None or head1.next == None:
        return head1
    if head2 == None or head2.next == None:
        return head2
    cur1 = head1.next
    cur2 = head2.next
    head = None
    cur = None
    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next
    while cur1 != None and cur2 != None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    # 当遍历完一个链表之后，把另一个链表剩余的节点的链接到合并之后的链表后面
    if cur1 == None:
        cur.next = cur2
    if cur2 == None:
        cur.next = cur1
    return head


if __name__ == '__main__':
    head1 = constructList(1)
    head2 = constructList(2)
    Print(0, head1)
    Print(0, head2)
    head = Merge(head1, head2)
    Print(2, head)
