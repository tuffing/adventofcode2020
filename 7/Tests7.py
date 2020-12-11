#!/usr/bin/python3
import sys
import unittest
#replace Day7 with day name
import Day7

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput7.txt!
                input_list = common.loadInput('testInput7.txt', True)
                testObject = Day7.Solution()
                testObject.generate_graph(input_list)
                self.assertEqual(4, testObject.part1())
                self.assertEqual(32, testObject.part2())

        def test_run2(self):
                input_list = common.loadInput('testInput7-2.txt', True)
                testObject = Day7.Solution()
                testObject.generate_graph(input_list)
                self.assertEqual(126, testObject.part2())

if __name__ == '__main__':
        unittest.main()