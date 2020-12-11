#!/usr/bin/python3
import sys
import unittest
#replace standard with day name
import standard

sys.path.append('../')
from scaffolding import common

class SolutionTest(unittest.TestCase):

        def test_run(self):
                #remember to set the assert to the known examples and place the example test into testInput.txt!
                input_list = common.loadInput('testInput.txt', True)
                self.assertEqual(138, standard.Solution.part1(input_list))


if __name__ == '__main__':
        unittest.main()