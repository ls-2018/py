"""
用 1、2、2、3、4、5打印出所有的排列组合；要求4 不能在第三位， 3、5不能相连

1、这6个数作为结点，构造一个无向连通图。   除了3 5 不能连通外，其他所有结点两两相连
2、分别从这6个结点出发对图做深度优先遍历，遍历完的结果记录下来，如果这个数字的第三位不是   4，那么把这个数字存放到集合Set中。
3、遍历Set集合，打印集合中的结果
"""


class Test:
    def __init__(self, arr):
        self.numbers = arr
        # 用来标记图中结点是否被遍历过
        self.visited = [False] * len(self.numbers)

        # 图的二维数组表示,可以连接的结点
        self.graph = [([0] * len(self.numbers)) for i in range(len(self.numbers))]
        self.n = 6

        # 数字的组合
        self.combination = ''

        # 存放所有的组合
        self.s = set()

    def depthFirstSearch(self, start):
        """
        对图从结点start位置开始进行深度遍历
        :param start:  遍历的起始位置
        """
        # 512234
        self.visited[start] = True  # 进入递归标记已用
        self.combination += str(self.numbers[start])  # 512234
        if len(self.combination) == self.n:
            # 4不出现在第三个位置
            if self.combination.index("4") != 2:
                self.s.add(self.combination)
        j = 0
        while j < self.n:
            if self.graph[start][j] == 1 and self.visited[j] == False:
                self.depthFirstSearch(j)
            j += 1
        self.combination = self.combination[:-1]    # 每退出一次递归，就减少一个，当完全退出以后，就是空字符串，可以方便最外层使用：因为最外层需要为空
        self.visited[start] = False  # 退出递归标记解除

    def getAllCombination(self):
        """
        用 1、2、2、3、4、5打印出所有的排列组合；要求4 不能在第三位， 3、5不能相连
        """
        # 构造图

        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if i == j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j] = 1
                j += 1
            i += 1
        # 确保在遍历的时候3 与5 是不可达的；35在数组中的位置，恰好是3  5
        self.graph[3][5] = 0
        self.graph[5][3] = 0
        # 分别从不同的结点出发深度遍历图
        i = 0
        while i < self.n:
            self.depthFirstSearch(i)
            i += 1

    def printAllCombinations(self):
        for strs in self.s:
            print(strs)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 5]
    t = Test(arr)
    t.getAllCombination()
    t.printAllCombinations()
