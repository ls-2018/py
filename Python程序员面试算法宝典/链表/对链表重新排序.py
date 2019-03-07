'''
L0  L1  L2   L3
  L7   L6  L5   L4
'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


'''
找出链表Head的中间结点,把链表从中间断成两个子链表
'''


def FindMiddleNode(head):
    if head is None or head.next is None:
        return head
    fast = head  # 遍历链表的时候每次向前走两步
    slow = head  # 遍历链表的时候每次向前走一步
    slowPre = head

    # 当fast到链表尾时，slow恰好指向链表的中间结点
    while fast is not None and fast.next is not None:
        slowPre = slow
        slow = slow.next
        fast = fast.next.next
    # 把链表断成两个链表
    slowPre.next = None
    return slow


def Reverse(head):
    if head == None or head.next == None:
        return head
    pre = head  # 前驱结点
    cur = head.next  # 当前节点
    next = cur.next  # 后继节点
    pre.next = None
    # 使当前遍历到的结点cur指向其前驱结点
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    return pre


def Recorder(head):
    if head == None or head.next == None:
        return
    # 前半部分链表的第一个结点
    cur1 = head.next
    mid = FindMiddleNode(cur1)
    # 后半部分链表逆序后的第一个结点
    cur2 = Reverse(mid)

    tmp = None
    while cur1.next is not None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp

        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp
    cur1.next = cur2


if __name__ == '__main__':

    head = LNode()
    head.next = None

    tmp = None
    cur = head
    # 构造 链表
    i = 1
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur = head.next
    while cur is not None:
        print(cur.data, end='', sep='')
        cur = cur.next
    print()
    Recorder(head)

    cur = head.next
    while cur is not None:
        print(cur.data, end='', sep='')
        cur = cur.next
    print()
