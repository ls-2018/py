'''
把每K个相邻的的结点为一组进行翻转,如果生育结点不足K个,则不进行翻转
1-2-3-4-5-6-7
如果K为3
3-2-1-6-5-4-7

主要思路:
    首先把前K个结点看成一个子链表,采用前面介绍的方法进行翻转,把翻转后的子链表连接到头结点后面,然后把接下来的K个结点看成另外一个单独的链表进行翻转,
    把翻转后的子链表链接到上一个已经完成翻转后的子链表的后面.
sa
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


# 对不带头结点的单链表进行翻转
def reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    cur = head.next  # 当前遍历结点
    pre = head  # 当前结点的前驱结点
    next = cur.next  # 当前结点后继节点的后继结点
    pre.next = None

    while cur != None:
        next = cur.next
        cur.next = pre

        pre = cur
        # print(pre.data)
        cur = cur.next
        cur = next
    return pre


# 对链表Ｋ进行翻转
def ReverseK(head, k):
    if head == None or head.next == None or k < 2:
        return
    pre = head
    begin = head.next
    end = None
    pNext = None
    i = 1
    while begin != None:
        end = begin
        while i < k:
            if end.next != None:
                end = end.next
            else:  # 剩余结点小于Ｋ
                return
            i += 1

        pNext = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = pNext
        pre = begin
        begin = pNext
        i = 1
        Print(1,head)


if __name__ == '__main__':
    i = 1
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
    Print(0, head)

    ReverseK(head, 3)
    Print(2, head)
# ９、如何把链表以K个结点为一组进行翻转