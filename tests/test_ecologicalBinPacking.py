from unittest import TestCase
from EcologicalBinPacking.EcologicalBinPacking import EcologicalBinPacking
import filecmp

class TestEcologicalBinPacking(TestCase):
    def test_print_optimal_movement(self):
        input_file = "EcologicalBinPacking/TestCases.txt"
        expect = "EcologicalBinPacking/expect.txt"
        output = "EcologicalBinPacking/output.txt"
        EcologicalBinPacking().print_optimal_movement(input_file, output)
        self.assertTrue(filecmp.cmp(expect,output,shallow=False))
