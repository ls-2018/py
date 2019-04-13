import unittest
import sys


class MyClassTest(unittest.TestCase):

    def test_add(self):

        ret = 2252
        self.assertEqual(ret, 225)

    def tearDown(self):
        print(self._outcome.errors,'--------')
        # [(<x.MyClassTest testMethod=test_add>,
        # (<class 'AssertionError'>,
        # AssertionError('2252 != 225',),
        # <traceback object at 0x0000024F9BC57F48>))] --------


if __name__ == '__main__':
    unittest.main()  # 命令行运行
