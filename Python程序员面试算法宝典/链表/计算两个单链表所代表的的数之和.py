'''
head->3->1->5
head->5->9->2
输出： 8-》0-》8
即 513+295=808
注意个位数在链表头

'''


# 方法一；整数相加法
# 方法二：链表相加法


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


def add(h1, h2):
    if h1 is None or h1.next is None:
        return
    if h2 is None or h2.next is None:
        return
    c = 0  # 用来记录进位
    sums = 0  # 用来记录两个结点相加的值
    p1 = h1.next  # 用来遍历h1
    p2 = h2.next  # 用来遍历h2
    tmp = None  # 用来指向新创建的存储相加的和的结点
    resultHead = LNode()  # 相加后链表头结点
    resultHead.next = None
    p = resultHead  # 用来指向链表resultHead最后一个结点
    while p1 is not None and p2 is not None:
        tmp = LNode()
        tmp.next = None
        sums = p1.data + p2.data + c
        tmp.data = sums % 10  # 两节点相加和
        c = sums // 10  # 进位
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next
    if p1 is None:
        while p2 is not None:
            tmp = LNode()
            tmp.next = None
            sums = p2.data + c
            tmp.data = sums % 10
            c = sums // 10
            p.next = tmp
            p = tmp
            p2 = p2.next
    if p2 is None:
        while p1 is not None:
            tmp = LNode()
            tmp.next = None
            sums = p1.data + c
            tmp.data = sums % 10
            c = sums // 10
            p.next = tmp
            p = tmp
            p1 = p1.next

    # 处理完之后还有进位
    if c == 1:
        tmp = LNode()
        tmp.next = None
        tmp.data = 1
        p.next = tmp
    return resultHead


if __name__ == '__main__':

    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None

    tmp = None
    cur = head1
    addResult = None
    # 构造第一个链表
    i = 1
    while i < 7:
        tmp = LNode()
        tmp.data = i + 2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    cur = head2
    # 构造第二个链表
    i = 9
    while i > 4:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i -= 1

    cur = head1.next
    while cur is not None:
        print(cur.data, end='', sep='')
        cur = cur.next
    print()
    cur = head2.next
    while cur is not None:
        print(cur.data, end='', sep='')
        cur = cur.next
    print()
    addResult = add(head1, head2)

    cur = addResult.next
    while cur is not None:
        print(cur.data, end='', sep='')
        cur = cur.next
