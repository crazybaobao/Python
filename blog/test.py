import unittest

from First_Project import calculator


class test(unittest.TestCase):
    def setUp(self):
        print("Test start!")

    def test_应老板是高手(self):
        j = calculator(4, 2)
        self.assertEqual(j.myadd(), 6)
        self.assertEqual(j.mydivide(), 2)

    def test_应老板玩田鸡(self):
        j = calculator(4, 0)
        self.assertEqual(j.mydivide(), 0)

    def test_应老板带我们飞(self):
        self.assertEqual(1, 2)

    def tearDown(self):
        print("Test end!")
