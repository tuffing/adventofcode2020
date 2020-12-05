#!/usr/bin/python3
import sys
import unittest
#replace Day3 with day name
import Day3

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput3.txt!
                input_list = common.loadInput('testInput3.txt', True)
                testObject = Day3.Solution()
                self.assertEqual(7, testObject.part1(input_list))

        def test_run_pt2(self):
                input_list = common.loadInput('testInput3.txt', True)
                testObject = Day3.Solution()
                self.assertEqual(336, testObject.part2(input_list))


if __name__ == '__main__':
        unittest.main()