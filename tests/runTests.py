import sys
import unittest
from threeNAndOne import ThreeNAndOne

if __name__ == '__main__':
    test_names = ['test_threeNAndOne']
    suite = unittest.defaultTestLoader.loadTestsFromNames ([t for t in test_names])
    result = unittest.TextTestRunner().run (suite)