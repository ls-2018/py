'''
1 2 3 4 5 6 7
2 1 4 3 6 5 7
# 方法一:
    交换数据域
# 方法二:
    就地逆序
    通过调整结点指针域的指向来直接调换相邻的两个结点,
        如果单链表恰好有偶数个结点,那么只需要将奇偶结点对调,
        如果单链表恰好有奇数个结点,那么只需要将最后一个结点外的其他结点进行奇偶对调即可
pre       cur             next
head       1       2       3       4       5
           pre            cur             next
'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


# 把链表相邻元素翻转
def reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return
    cur = head.next  # 当前遍历结点
    pre = head  # 当前结点的前驱结点
    next = None  # 当前结点后继节点的后继结点
    while cur != None and cur.next != None:
        # next =cur.next
        # pre.next = next
        # pre = next
        # next
        next = cur.next.next
        pre.next = cur.next  # 奇数 指向 偶数
        cur.next.next = cur  # (奇数指向偶数)指向前驱结点
        cur.next = next  # 奇数指向奇数

        pre = cur       # 翻转之后,cur就是前驱结点
        # print(pre.data)
        cur = next


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
    Print(0,head)

    reverse(head)
    Print(2,head)
