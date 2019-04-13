import unittest
import HTMLTestRunner


class MyClassTest(unittest.TestCase):

    def test_add(self):
        ret = 225
        self.assertEqual(ret, 225)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyClassTest('test_add'))
    fp = open(r'D:\Destop\book\Flask－\my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.',
        verbosity=2
    )
    runner.run(suite)           #  命令行运行
