# assert  断言
# 若是False直接终止程序
# assert 1+2>6

#常用的python单元测试库： unitest （对软件中的最小可测试单元进行验证）、
#开发代码最好和测试代码分开一个文件
import unittest
from test import my_adder,TestClass

# 測試用例 (testcase) 可以透過繼承 unittest.TestCase 類別來建立。
# https://docs.python.org/zh-tw/dev/library/unittest.html
# 這裡定義了三個獨立的物件方法，名稱皆以 test 開頭。
# 這樣的命名方式能告知 test runner 哪些物件方法為定義的測試。
class TestMyAdder(unittest.TestCase):
    # 在运行各个方法，也就是test_开头的方法前，setUp方法都会先被执行一次
    def setUp(self):
        self.content_len = TestClass('单元测试')
        print(self.content_len)
    def test_positive_with_positive(self):
        # 1. assertEqual() # 來確認是否為期望的結果；
        # 2. assertTrue()或是assertFalse()用來驗證一個條件式；
        # 3. assertRaises() 用來驗證是否觸發一個特定的exception。
        # 使用這些物件方法來取代assert 陳述句，將能使test runner 收集所有的測試結果並產生一個報表。
        self.assertEqual(self.content_len.len_count(),8)

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)

# 终端运行 python -m unittest -v unit_test.py 可得到测试结果 或者 直接运行代码
