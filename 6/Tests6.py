#!/usr/bin/python3
import sys
import unittest
#replace Day6 with day name
import Day6

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput6.txt!
                input_list = common.loadInput('testInput6.txt', False)
                self.assertEqual(11, Day6.Solution.part1(input_list))
                self.assertEqual(6, Day6.Solution.part2(input_list))


if __name__ == '__main__':
        unittest.main()