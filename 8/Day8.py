#!/usr/bin/python3

import sys
import collections
sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self, program):
        self.currentProgram = program
        self.accumulator = 0
        self.pos = 0

    def part1(self):
        visited = set()

        while 0 <= self.pos <= len(self.currentProgram):
            if self.pos in visited:
                return self.accumulator

            visited.add(self.pos)
            cmd, value = self.currentProgram[self.pos].split(' ')
            getattr(self, cmd)(int(value))

        return -1

    def part2(self):
        # one of the nops or jmps are inverted.
        # try them all until one doesn't cause an infinite loop.
        for i in range(0, len(self.currentProgram)):
            visited = collections.Counter()
            recurse_check = 2
            self.pos = 0
            self.accumulator = 0

            if self.currentProgram[i][0:3] not in ['jmp', 'nop']:
                continue

            while 0 <= self.pos < len(self.currentProgram):
                visited[self.pos] += 1

                if visited[self.pos] >= recurse_check:
                    break

                cmd, value = self.currentProgram[self.pos].split(' ')
                if self.pos == i:
                    if cmd == 'jmp':
                        cmd = 'nop'
                    elif cmd == 'nop':
                        cmd = 'jmp'

                getattr(self, cmd)(int(value))

            if self.pos < 0 or len(self.currentProgram) <= self.pos:
                return self.accumulator

        return -1

    def acc(self, value):
        self.accumulator = self.accumulator + value
        self.pos = self.pos + 1

    def jmp(self, value):
        self.pos = self.pos + value

    def nop(self, value):
        self.pos = self.pos + 1

    def run(self):
        print('Advent Day: Day8')
        p1 = self.part1()
        print('Part1: %s' % str(p1))
        p2 = self.part2()
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    input_list = common.loadInput('input8.txt', True)

    Solution(input_list).run()
