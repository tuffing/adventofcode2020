#!/usr/bin/python3

import sys
import math

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(input_list):
        results = list(map(lambda s: Solution.follow_directions(s), input_list))
        return max(results)

    @staticmethod
    def find_middle(directions: str, min_s, max_s):
        for c in directions:
            if c in ['F', 'L']:
                max_s = min_s + math.floor((max_s - min_s) / 2)
            if c in ['B', 'R']:
                min_s = min_s + math.ceil((max_s - min_s) / 2)

        return min_s

    @staticmethod
    def find_id(row, col):
        return (row * 8) + col

    @staticmethod
    def follow_directions(directions: str):
        row = Solution.find_middle(directions[0:7], 0, 127)
        col = Solution.find_middle(directions[7:], 0, 7)
        return Solution.find_id(row, col)

    @staticmethod
    def part2(input_list):
        results = set(map(lambda s: Solution.follow_directions(s), input_list))
        for x in range(min(results), max(results)):
            if x not in results:
                return x
        return -1

    def run(self):
        input_list = common.loadInput('input5.txt', True)
        print('Advent Day: Day5')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
