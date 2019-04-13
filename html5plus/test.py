demo = {}
print(sum(demo.values()))


import unittest
import os
class RunCase(unittest.TestCase):
    def test(self):
        case_path = '.....'
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

# 运行所有的测试文件
if __name__ == '__main__':
    unittest.main()

