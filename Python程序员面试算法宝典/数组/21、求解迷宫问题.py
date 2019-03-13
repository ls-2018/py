"""
申请一个结果矩阵来标记移动的路径
if  到达了目的地
    打印解决方案矩阵
else
    在结果矩阵中标记当前为1（移动的路径）
    向右前进一步，然后递归检查，检查完这一步，判断是否存在终点的可达路线
    如果步骤2中的移动方法导致没有通往终点的路径，那么选择向下移动一步，然后检查使用这种移动方法后，是否存在到终点的可达的路线
    如果上面的移动方法后悔导致没有可达的路径，那么标记当前单元格在结果矩阵中为0，返回false，并回溯到前一步中。
"""


class Maze:
    def __init__(self):
        self.N = 4

    # 打印从起点到终点的路线
    def printSolution(self, sol):
        i = 0
        while i < self.N:
            j = 0
            while j < self.N:
                print(sol[i][j], end=' ')
                j += 1
            print()
            i += 1

    def isSafe(self, maze, x, y):
        # 判断x和y是否是一个合理的单元
        return 0 <= x < self.N and 0 <= y < self.N and maze[x][y] == 1

    def getPath(self, maze, x, y, sol):
        """
        使用回溯方法从左上角找到一条到右下角的路径
        :param maze: 迷宫
        :param x: 起点
        :param y: 起点
        :param sol: 解决方案
        :return:
        """
        if x == self.N - 1 and y == self.N - 1:  # 到达目的地
            sol[x][y] = 1
            return True
        # 判断maze[x][y]是否是一个可走的单元
        if self.isSafe(maze, x, y):
            # 标记当前单元为1
            sol[x][y] = 1
            # 向右走一步
            if self.getPath(maze, x + 1, y, sol):
                return True
            # 向下走一步
            if self.getPath(maze, x, y + 1, sol):
                return True
            # 标记当前单元为0用来表示这条路不可行，然后回溯
            sol[x][y] = 0
            return False
        return False


if __name__ == '__main__':
    rat = Maze()
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ]
    sol = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    if not rat.getPath(maze, 0, 0, sol):
        print('不可达')
    else:
        rat.printSolution(sol)

if __name__ == '__main__':
    pass
