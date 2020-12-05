#!/usr/bin/python3
#
import os
import sys
from typing import TextIO


class MakeDay(object):

    @staticmethod
    def generate(day_name):
        # dir is not keyword
        def create_dir(name):
            try:
                os.makedirs(name)
            except OSError:
                pass

        create_dir(day_name)

        path = os.path.dirname(os.path.abspath(__file__))
        # solution files
        class_name = 'Day%s' % day_name

        files = {'standard.py': 'Day%s.py',
                 'solutionTest.py': 'Tests%s.py',
                 'testInput.txt': 'testInput%s.txt',
                 'input.txt': 'input%s.txt'
                 }
        for key in files:
            input_file: TextIO = open('%s\\scaffolding\\%s' % (path, key), 'r')
            day_code = input_file.read()
            day_code = day_code.replace('standard', class_name)
            day_code = day_code.replace('input.txt', 'input%s.txt' % day_name)
            day_code = day_code.replace('testInput.txt', 'testInput%s.txt' % day_name)
            input_file.close()

            input_file = open('%s\\%s\\%s' % (path, day_name, files[key] % day_name), 'w')
            input_file.write(day_code)
            input_file.close()

        print('generated day %s' % day_name)


if __name__ == '__main__':
    MakeDay().generate(sys.argv[1])
