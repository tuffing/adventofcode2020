#!/usr/bin/python3
import sys
import functools

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(mt_map, move_x=3, move_y=1):
        coord = (0, 0)
        count = 0

        while coord[1] < len(mt_map):
            if mt_map[coord[1]][coord[0]] == '#':
                count = count + 1
            coord = Solution.move_sled(len(mt_map[0]), coord[0], coord[1], move_x, move_y)

        return count

    @staticmethod
    def move_sled(map_width, curr_x, curr_y, move_x, move_y):
        return (curr_x + move_x) % map_width, curr_y + move_y

    @staticmethod
    def part2(mt_map):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        results = list(map(lambda s: Solution.part1(mt_map, s[0], s[1]), slopes))
        return functools.reduce(lambda a, b: a*b, results)

    def run(self):
        input_list = common.loadInput('input3.txt', True)
        print('Advent Day: X')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
