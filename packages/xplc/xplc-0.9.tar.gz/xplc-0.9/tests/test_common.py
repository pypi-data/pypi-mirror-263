import unittest
from xplc.__main__ import func1


class TestCommon(unittest.TestCase):
    def test_sum(self):
        self.assertTrue(2 + 2 == 4)

    def test_func1(self):
        self.assertTrue(func1(2,3) == 5)


if __name__ == '__main__':
    unittest.main()
