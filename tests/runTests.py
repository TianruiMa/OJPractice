import unittest

if __name__ == '__main__':
    blocks_problem = 'test_blocksProblem'
    three_n_and_one = 'test_threeNAndOne'
    bin_packing = 'test_ecologicalBinPacking'
    test_names = [bin_packing]
    suite = unittest.defaultTestLoader.loadTestsFromNames ([t for t in test_names])
    result = unittest.TextTestRunner().run (suite)