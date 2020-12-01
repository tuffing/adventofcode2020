#!/usr/bin/python3

import sys
sys.path.append('../')
from scaffolding import common

class Solution(object):
	def __init__(self):
		pass

	def solution(self, inputNumbers):
		i = list(map(lambda x: int(x), inputNumbers))

		for x in range(0, len(inputNumbers)):
			for y in range(x, len(inputNumbers)):
				for z in range(y, len(inputNumbers)):
					if i[x] + i[y] + i[z] == 2020:
						print('%d %d %d' % (i[x] , i[y] , i[z]))
						return i[x] * i[y] * i[z]

		return -1

	def run(self):
		inputList = common.loadInput('input.txt', True) #True = split, False = string
		print('Advent Day: X')
		print(self.solution(inputList))



if __name__ == '__main__':
	Solution().run()
