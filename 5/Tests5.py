#!/usr/bin/python3
import sys
import unittest
#replace Day5 with day name
import Day5

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput5.txt!
                #input_list = common.loadInput('testInput5.txt', True)
                self.assertEqual(44, Day5.Solution.find_middle('FBFBBFF', 0, 127))
                self.assertEqual(5, Day5.Solution.find_middle('RLR', 0, 7))
                self.assertEqual(357, Day5.Solution.find_id(44, 5))
                self.assertEqual(357, Day5.Solution.follow_directions('FBFBBFFRLR'))


if __name__ == '__main__':
        unittest.main()