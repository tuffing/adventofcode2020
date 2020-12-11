#!/usr/bin/python3

import sys
import re
import functools

sys.path.append('../')
from scaffolding import common
import collections

class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(input_list):
        groups = re.split(r'\n\n', input_list)
        return sum(map(lambda g: len(set(g.replace('\n', ''))), groups))

    @staticmethod
    def part2(input_list):
        groups = re.split(r'\n\n', input_list)
        count = 0

        for g in groups:
            uniques = collections.Counter(g.replace('\n', ''))
            count = count + len(list(filter(lambda x: uniques[x] == len(g.split('\n')), uniques)))
        return count

    def run(self):
        input_list = common.loadInput('input6.txt', False)
        print('Advent Day: Day6')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
