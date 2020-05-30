import unittest
from main import Solution

class TestCase(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(True, s.canFinish(2, [[1, 0]]))
        self.assertEqual(False, s.canFinish(2, [[1, 0], [0, 1]]))

