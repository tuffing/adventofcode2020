#!/usr/bin/python3
import sys
import unittest
# replace Day9 with day name
import Day9

sys.path.append('../')
from scaffolding import common


class SolutionTest(unittest.TestCase):

    def test_run(self):
        numbers = common.loadInput('testInput9.txt', True)
        self.assertEqual(Day9.Solution.part1(numbers, 5), 127)
        numbers = common.loadInput('testInput9-2.txt', True)
        self.assertEqual(Day9.Solution.part2(numbers, 127), 62)


if __name__ == '__main__':
    unittest.main()
