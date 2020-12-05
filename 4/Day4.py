#!/usr/bin/python3

import sys
import re

sys.path.append('../')
from scaffolding import common


class Solution(object):

    def __init__(self):
        pass

    @staticmethod
    def part1(passport_str):
        passports = Solution.build_passport_list(passport_str)
        count = len(passports)

        for p in passports:
            if len(p) < 7 or (len(p) == 7 and 'cid' in p):
                count = count - 1

        return count

    @staticmethod
    def build_passport_list(passport_string):
        singles = re.split(r'\n\n', passport_string)
        passports = []

        for p in singles:
            passport = dict()
            elements = re.findall(r'[a-z]+:[^\s\n]+', p)
            for e in elements:
                split = e.split(':')
                passport[split[0]] = split[1]

            passports.append(passport)

        return passports

    @staticmethod
    def part2(passport_str):
        passports = Solution.build_passport_list(passport_str)
        count = 0

        for p in passports:
            if Solution.is_valid(p):
                count = count + 1
                # print(p)

        return count

    @staticmethod
    def is_valid(passport: dict):
        """    byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not."""
        if len(passport) < 7 or (len(passport) == 7 and 'cid' in passport):
            return False

        if not (1920 <= int(passport['byr']) <= 2002) or len(passport['byr']) != 4:
            return False

        if not (2010 <= int(passport['iyr']) <= 2020) or len(passport['iyr']) != 4:
            return False

        if not (2020 <= int(passport['eyr']) <= 2030) or len(passport['eyr']) != 4:
            return False

        if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'].replace('cm', '')) <= 193):
            return False
        elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'].replace('in', '')) <= 76):
            return False
        elif 'in' not in passport['hgt'] and 'cm' not in passport['hgt']:
            return False

        if not re.match(r'^\#[\da-f]{6}$', passport['hcl']):
            return False

        if len(passport['ecl']) != 3 or passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False

        if not re.match(r'^\d{9}$', passport['pid']):
            return False

        return True

    def run(self):
        input_list = common.loadInput('input4.txt', False)
        print('Advent Day: Day4')
        p1 = self.part1(input_list)
        print('Part1: %s' % str(p1))
        p2 = self.part2(input_list)
        print('Part2: %s' % str(p2))


if __name__ == '__main__':
    Solution().run()
