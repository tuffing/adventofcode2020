#!/usr/bin/python3
import sys
import unittest
#replace Day4 with day name
import Day4

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                input_list = common.loadInput('testInput4.txt', False)
                testObject = Day4.Solution()
                self.assertEqual(2, testObject.part1(input_list))

        def test_run_pt2(self):
                input_list = common.loadInput('testInput4-p2.txt', False)
                testObject = Day4.Solution()
                self.assertEqual(4, testObject.part2(input_list))



if __name__ == '__main__':
        unittest.main()