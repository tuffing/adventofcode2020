#!/usr/bin/python3
import sys
import unittest
#replace Day10 with day name
import Day10

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        '''def test_run(self):
                input_list = common.loadInput('testInput10.txt', True)
                self.assertEqual(7*5, Day10.Solution.part1(input_list))

                input_list = common.loadInput('testInput10-2.txt', True)
                self.assertEqual(22*10, Day10.Solution.part1(input_list))'''


        def test_run_2(self):
                input_list = common.loadInput('testInput10.txt', True)
                self.assertEqual(8, Day10.Solution.part2(input_list))

                input_list = common.loadInput('testInput10-2.txt', True)
                self.assertEqual(19208, Day10.Solution.part2(input_list))

if __name__ == '__main__':
        unittest.main()