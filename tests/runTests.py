import sys
import unittest
from threeNAndOne import ThreeNAndOne

if __name__ == '__main__':
    blocks_problem = 'test_blocksProblem'
    three_n_and_one = 'test_threeNAndOne'
    test_names = [blocks_problem]
    suite = unittest.defaultTestLoader.loadTestsFromNames ([t for t in test_names])
    result = unittest.TextTestRunner().run (suite)