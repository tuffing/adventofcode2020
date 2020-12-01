#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common


class Solution(object):
	#inputNumbers = common.pullNumbersFromList(inputList, True) #True = include signs, False: all numbers are positive

	def __init__(self):
		pass

	def solution(self, inputNumbers):
		inputNumbers = list(map(lambda x: int(x), inputNumbers))

		while len(inputNumbers):
			y = inputNumbers.pop()
			result = list(filter(lambda x: x + y == 2020, inputNumbers))

			if len(result) > 0:
				return y * list(result)[0]

		return -1

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		print(self.solution(inputList))



if __name__ == '__main__':
	Solution().run()
