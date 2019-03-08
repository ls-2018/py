'''
head 1 2 3 4
              5  6  7
head 1 2 3 4
# 判断是否交叉,如果相交，找出相同的结点
# 方法一：
    n^n次遍历
# 方法二：
    首尾相接法--->将一个链表的头和另一个链表的尾链接,判断是否是一个环
# 方法三：
    尾结点法：　如果两个链表有交叉，那么链表的最后一个结点肯定一样，这时记下两个链表的长度n1.n2，再遍历一次，长链表结点先出发｜n1-n2｜
    之后两个链表同时前进，每次一步，相遇的第一个点即为两个链表相交的第一个点

'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


def IsInstance(head1, head2):
    if head1 == None or head1.next == None or head2 == None or head2.next == None or head2 == head1:
        return None
    temp1 = head1.next
    temp2 = head2.next
    n1 = n2 = 0
    while temp1.next != None:
        temp1 = temp1.next
        n1 += 1

    while temp2.next != None:
        temp2 = temp2.next
        n2 += 1

    if temp1 == temp2:
        if n1 > n2:
            while n1 - n2 > 0:
                head1 = head1.next
                n1 -= 1
        if n2 > n1:
            while n2 - n1 > 0:
                head2 = head2.next
                n2 -= 1

        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None


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
    i = 0
    while cur != None and i < 10:
        print('->', cur.data, end='', sep='')
        cur = cur.next
        i += 1
    print()


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


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head1.next = None

    head2 = LNode()
    head2.next = None

    tmp = None
    cur = head1
    p = None

    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    Print(0, head1)
    cur = head2

    i = 1
    while i < 5:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = p
    Print(0, head2)

    innerNode = IsInstance(head1, head2)
    if innerNode == None:
        print('不相交')
    else:
        print('相交', innerNode.data)
