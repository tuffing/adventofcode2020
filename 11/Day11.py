#!/usr/bin/python3

import sys

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(m):
        old_hash = ''
        for r in m:
            old_hash += r

        for i in range(300):
            new_m = Solution.tick(m)
            new_hash = ''
            for r in new_m:
                new_hash += r

            if new_hash == old_hash:
                return new_hash.count('#')

            old_hash = new_hash
            m = new_m

    @staticmethod
    def part2(input_list):
        print('Solution Here')
        return 2

    @staticmethod
    def tick(m):
        new_map = [("." * len(m[0])) for _ in range(len(m))]
        # top, topright, right, bottomright, bottom, bottomleft, left, topleft
        # x,y
        angles = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

        for y, row in enumerate(m):
            for x, spot in enumerate(row):
                occ_count = 0
                emp_count = 0
                if m[y][x] == '.':
                    continue

                for mx, my in angles:
                    if 0 <= y+my < len(m) and 0 <= x+mx < len(m[0]):
                        if m[y + my][x + mx] in ['L', '.']:
                            emp_count += 1
                        if m[y + my][x + mx] == '#':
                            occ_count += 1
                    else:
                        emp_count += 1

                if m[y][x] == '#':
                    new_map[y] = new_map[y][:x] + '#' + new_map[y][x + 1:]
                    if occ_count >= 4:
                        new_map[y] = new_map[y][:x] + 'L' + new_map[y][x + 1:]

                if m[y][x] == 'L':
                    new_map[y] = new_map[y][:x] + 'L' + new_map[y][x + 1:]
                    if emp_count == 8:
                        new_map[y] = new_map[y][:x] + '#' + new_map[y][x + 1:]

        return new_map







    def run(self):
        input_list = common.loadInput('input11.txt', True)
        print('Advent Day: Day11')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
