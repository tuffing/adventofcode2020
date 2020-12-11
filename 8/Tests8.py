#!/usr/bin/python3
import sys
import unittest
#replace Day8 with day name
import Day8

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput8.txt!
                input_list = common.loadInput('testInput8.txt', True)
                self.assertEqual(5, Day8.Solution(input_list).part1())


if __name__ == '__main__':
        unittest.main()