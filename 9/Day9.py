#!/usr/bin/python3

import sys

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(numbers, preamble):
        numbers = list(map(int, numbers))
        usable = set(numbers[0:preamble])

        for i in range(preamble, len(numbers)):
            for x in usable:
                if numbers[i] - x in usable:
                    usable.add(numbers[i])
                    break
            usable.remove(numbers[i - preamble])

            if len(usable) < preamble:
                return numbers[i]
        return -1

    @staticmethod
    def part2(numbers, target):
        numbers = list(map(int, numbers))

        while len(numbers):
            total = target
            for i, n in enumerate(numbers):
                total -= n
                if total < 0:
                    break

                if total == 0:
                    return min(numbers[0:i+1]) + max(numbers[0:i+1])

            numbers.pop(0)

        return -1

    def run(self):
        input_list = common.loadInput('input9.txt', True)
        print('Advent Day: Day9')
        p1 = self.part1(input_list, 25)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list, p1)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
