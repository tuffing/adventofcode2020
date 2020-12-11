#!/usr/bin/python3

import sys
import re
import collections

sys.path.append('../')
from scaffolding import common


class Bag(object):
    def __init__(self, name):
        self.name: str = name
        self.children = collections.Counter()
        self.parents = set()

    def __str__(self):
        return self.name

    def print(self):
        print('----%s-----' % self.name)
        print(self.bags)
        print('--Parents--')
        print(self.parents)


class Solution(object):

    def __init__(self):
        self.bags = dict()

    def part1(self):
        to_check = [self.bags['shiny gold']]

        parents = set()
        while len(to_check):
            bag = to_check.pop()
            parents.update(bag.parents)
            to_check.extend(bag.parents)

        return len(parents)

    def part2(self):
        to_check = ['shiny gold']

        count = 0
        while len(to_check):
            bag = self.bags[to_check.pop()]
            for c in bag.children:
                for i in range(0, bag.children[c]):
                    to_check.append(c)

            count = count + sum(bag.children.values())

        return count

    def generate_graph(self, input_list):
        for i in input_list:
            res = re.findall(r'([0-9]*)\s?([a-z\s]+)\sbag', i)
            first = res.pop(0)
            if first[1] not in self.bags:
                self.bags[first[1]] = Bag(first[1])

            working_bag = self.bags[first[1]]

            for r in res:
                if r[1] not in self.bags:
                    self.bags[r[1]] = Bag(r[1])
                self.bags[r[1]].parents.add(working_bag)

                if int(r[0]) > 0:
                    working_bag.children[r[1]] = int(r[0])

    def run(self):
        input_list = common.loadInput('input7.txt', True)
        print('Advent Day: Day7')
        self.generate_graph(input_list)
        p1 = self.part1()
        print('Part1: %s' % str(p1))
        p2 = self.part2()
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
