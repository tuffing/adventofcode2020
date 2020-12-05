#!/usr/bin/python3

import sys
import re

sys.path.append('../')
from scaffolding import common
import collections


class Solution(object):

	def __init__(self):
		pass

	def solution(self, inputList):
		count = 0
		for line in inputList:
			limits = list(map(int, re.findall(r'\d+', line)))
			start = re.search("([a-z]):", line)
			letters = collections.Counter(list(line))

			if limits[0] <= letters[start.groups()[0]] - 1 <= limits[1]:
				count = count + 1

		return count

	def run(self):
		inputList = common.loadInput('input.txt', True)  # True = split, False = string
		print('Advent Day: X result: %d' % self.solution(inputList))


if __name__ == '__main__':
	Solution().run()
