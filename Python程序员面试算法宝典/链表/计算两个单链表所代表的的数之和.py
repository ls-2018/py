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


def add():
    pass


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
        print(cur.data)
        cur=cur.next
    cur = head2.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    addResult = add(head1,head2)
    cur =addResult.next
    while cur is not None:
        print(cur.data)
        cur=cur.next