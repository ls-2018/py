class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None

    '''
    给定一个带头结点的单链表,将其逆序
    head->1->2->3->4->5->6->7
    head->7->6->5->4->3->2->1
    '''


def removeDup(head: LNode):
    if head == None or head.next == None:
        return
    outerCur = head.next  # 用于外层循环,指向链表的第一个结点
    innerCur = None  # 用于内层循环用来循环遍历outerCur后面的结点
    innerPre = None  # innerCur 的前驱结点
    while outerCur != None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur != None:
            # 找到重复的结点并删除
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        Print(1, head)
        outerCur = outerCur.next


def Print(flag, head):
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
    # 链表首结点
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    Print(0, head)
    removeDup(head)
    Print(2, head)
