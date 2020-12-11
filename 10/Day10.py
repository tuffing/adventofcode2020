#!/usr/bin/python3

import sys
import heapq

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(numbers):
        """
        Just a path algorithm at the end of the day.
        the optimisation for this version is to check if we've seeing number before, and this far along
        this results in fairly favourable speed. not usable in part 2 though.
        """
        numbers = set(sorted(map(int, numbers)))

        numbers.add(0)
        numbers.add(max(numbers) + 3)
        queue = [(0, 0, 0, set([0]))]
        highest = (0, 0)

        heapq.heapify(queue)

        while len(queue):
            cur, ones, threes, nums = heapq.heappop(queue)

            if cur == highest[0] and len(nums) < highest[1] and cur > 0:
                continue

            highest = max((cur, len(nums)), highest)

            for i in range(cur + 1, cur + 4):
                if i not in nums and i in numbers:
                    new_ones = ones
                    new_threes = threes
                    if i - cur == 1:
                        new_ones += 1
                    if i - cur == 3:
                        new_threes += 1

                    new_nums = nums.copy()
                    new_nums.add(i)

                    if i == highest[0] and len(new_nums) < highest[1] and i > 0:
                        continue

                    highest = max((i, len(new_nums)), highest)

                    if len(new_nums) == len(numbers):
                        return new_ones * new_threes

                    heapq.heappush(queue, (i, new_ones, new_threes, new_nums))

        return -1

    @staticmethod
    def part2(numbers):
        """
        Part2, as the largest gaps allowed are steps of 3,
        this approach finds where these steps are required.
        These represent bottlenecks in which all paths must follow,
        it's much faster to run these calculates up until each bottle neck, and then
        again between this bottle neck and the next. this signifcantly drops the number of
        steps required to get an answer. From potentially hours, into the microseconds.
        """
        numbers = set(sorted(map(int, numbers)))

        numbers.add(0)
        device = max(numbers) + 3
        numbers.add(device)

        prev = 0
        result = 1

        steps = [0]
        for i in sorted(numbers):
            if i - prev == 3:
                steps.append(prev)
            prev = i
        steps.append(device)

        for index, s in enumerate(steps):
            count = 0
            if s == device:
                return result
            queue = [(-s, s, set([s]))]

            heapq.heapify(queue)

            while len(queue):
                idx, cur, nums = heapq.heappop(queue)

                for i in range(cur + 1, cur + 4):
                    if i not in nums and i in numbers:
                        if i == steps[index+1]:
                            count += 1
                            break

                        new_nums = nums.copy()
                        new_nums.add(i)

                        heapq.heappush(queue, (-i, i, new_nums))

            result *= count

        return result

    def run(self):
        input_list = common.loadInput('input10.txt', True)
        print('Advent Day: Day10')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
