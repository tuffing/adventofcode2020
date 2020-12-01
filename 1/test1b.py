#!/usr/bin/python3

import unittest
import sys

from sol1b import *

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                inputList = common.loadInput('testInput.txt', True)
                testObject = Solution()
                self.assertEqual(241861950, testObject.solution(inputList))


if __name__ == '__main__':
        unittest.main()