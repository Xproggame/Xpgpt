import unittest
from Lecture import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        statistique(['test'], 1)
        self.assertListEqual(separation(True, True))


if __name__ == '__main__':
    unittest.main()
