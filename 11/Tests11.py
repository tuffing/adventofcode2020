#!/usr/bin/python3
import sys
import unittest
#replace Day11 with day name
import Day11

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                input_list = common.loadInput('testInput11.txt', True)
                self.assertEqual(37, Day11.Solution.part1(input_list))


if __name__ == '__main__':
        unittest.main()