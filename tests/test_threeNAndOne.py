from unittest import TestCase
from solution import solver


class TestThreeNAndOne(TestCase):
    # def test_three_n_and_one(self):
    #     with open("ThreeNAndOnes/TestCases.txt", "r") as inp:
    #         for line in inp:
    #             a, b, c = map(int, line.split())
    #             res = ThreeNAndOnes().three_n_and_one(a, b)
    #             self.assertEqual(res, c)
    #     file.close(inp)

    def test_solver(self):
        with open("UVaProblemSet/ThreeNAndOnes/TestCases.txt", "r") as inp:
            for line in inp:
                a, b, c = map(int, line.split())
                res = solver(a, b)
                self.assertEqual(res, c)
        file.close(inp)
