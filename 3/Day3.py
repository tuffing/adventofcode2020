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
        input_list = common.loadInput('input3.txt', True)
        print('Advent Day: X')
        self.part1(input_list)
        self.part2(input_list)


if __name__ == '__main__':
    Solution().run()
