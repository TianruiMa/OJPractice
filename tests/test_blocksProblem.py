from unittest import TestCase
from UVaProblemSet.TheBlocksProblem.BlocksProblem import BlocksProblem
import filecmp


class TestBlocksProblem(TestCase):
    def test_case_simple(self):
        input_file_name = "UVaProblemSet/TheBlocksProblem/TestCases.txt"
        output_file_name = "UVaProblemSet//TheBlocksProblem/output.txt"
        expect_file_name = "UVaProblemSet//TheBlocksProblem/expect.txt"
        block_game = BlocksProblem(input_file_name)
        block_game.actions(input_file_name, output_file_name)
        self.assertTrue(filecmp.cmp(output_file_name, expect_file_name, shallow=False))
