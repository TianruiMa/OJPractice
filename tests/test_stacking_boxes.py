from unittest import TestCase
from StackingBoxes import StackingBoxes
import filecmp

class TestStacking_Boxes(TestCase):
    def test_read_input(self):
        input_file_name = "StackingBoxes/TestCases.txt"
        output_file_name = "StackingBoxes/output.txt"
        expect_file_name = "StackingBoxes/expect.txt"
        StackingBoxes.read_input(input_file_name,output_file_name)
        self.assertTrue(filecmp.cmp(output_file_name,expect_file_name,shallow=False))
