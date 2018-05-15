from unittest import TestCase
from UVaProblemSet.EcologicalBinPacking import EcologicalBinPacking
import filecmp

class TestEcologicalBinPacking(TestCase):
    def test_print_optimal_movement(self):
        input_file = "UVaProblemSet//EcologicalBinPacking/TestCases.txt"
        expect = "UVaProblemSet//EcologicalBinPacking/expect.txt"
        output = "UVaProblemSet//EcologicalBinPacking/output.txt"
        EcologicalBinPacking.EcologicalBinPacking().print_optimal_movement(input_file, output)
        self.assertTrue(filecmp.cmp(expect,output,shallow=False))
