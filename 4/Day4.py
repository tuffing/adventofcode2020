#!/usr/bin/python3

import sys

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(input_list):
        print('Solution Here')
        return 1

    @staticmethod
    def part2(input_list):
        print('Solution Here')
        return 2

    def run(self):
        input_list = common.loadInput('input4.txt', True)
        print('Advent Day: Day4')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
