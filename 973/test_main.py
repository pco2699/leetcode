import unittest
from main import Solution

class TestCase(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
