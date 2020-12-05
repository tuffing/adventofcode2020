#!/usr/bin/python3

import sys
import re

sys.path.append('../')
from scaffolding import common

class Solution(object):

	def __init__(self):
		pass

	@staticmethod
	def solution(input_list):
		count = 0
		for line in input_list:
			goals = list(map(int, re.findall(r'\d+', line)))
			must_match = re.search("([a-z]):", line).groups()[0]
			letters = list(re.search(r'\s([a-z]+$)', line).groups()[0])

			if letters[goals[0] - 1] == letters[goals[1] - 1]:
				continue

			if must_match == letters[goals[0] - 1] or must_match == letters[goals[1] - 1]:
				count = count + 1

		return count

	def run(self):
		input_list = common.loadInput('input.txt', True)  # True = split, False = string
		print('Advent Day: X result: %d' % self.solution(input_list))


if __name__ == '__main__':
	Solution().run()
