from unittest import TestCase
from threeNAndOne import ThreeNAndOne


class TestThreeNAndOne(TestCase):
    def test_three_n_and_one(self):
        testInstance = ThreeNAndOne()
        with open("3N+1Problem/TestCases.txt", "r") as inp:
            for line in inp:
                a, b, c = map(int, line.split())
                res = testInstance.three_n_and_one(a, b)
                self.assertEqual(res, c)
        file.close(inp)
