"""
给定一趟旅程中所有的车票信息，根据这个车票信息找出这趟旅程的路线；
例如：
    （西安，成都），（北京，上海），（大连，西安），（上海，大连）
    -----》
    北京---上海----大连-----西安----成都
    假定给定的车票不会有环，也就是说有一个城市只作为终点而不会作为起点。

思路：
    根据车票信息构建一个字典，然后从这个字典中找到整个旅程的起点，接着就可以从起点出发一次找到下一站，进而知道重点。

    1、根据车票的出发地与目的地构建字典
    2、构建Tickets的逆向字典（起始点反向）
    3、遍历Tickets，对于遍历到的key值，判断这个是否在ReverseTickets中的key中存在，
        如果不存在，那么说明遍历到的Tickets中的key值就是路途的起点

"""


def printResult(inputs):
    # 用来存储把inputs的键与值调换后的信息
    reverseInput = dict()
    for k, v in inputs.items():
        reverseInput[v] = k
    start = None

    # 找到起点
    for k, v in inputs.items():
        if k not in reverseInput:
            start = k
            break
    if start == None:
        print('输入法不合理')
        return
    # 从起点出发按照顺序遍历路径
    to=inputs.get(start)
    while to != None:
        print(start, '--->', to)
        start = to
        to = inputs.get(to)


if __name__ == '__main__':
    inputs = dict()
    inputs['西安'] = '成都'
    inputs['北京'] = '上海'
    inputs['大连'] = '西安'
    inputs['上海'] = '大连'
    printResult(inputs)
