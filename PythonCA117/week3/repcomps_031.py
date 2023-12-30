#!/usr/bin/env python3

import sys
linest = sys.stdin.readlines()

def srgwsbvsfb(nums):
    line = range(1, nums + 1)
    line = list(line)
    multiof3g = ["X" if (n % 3 == 0) else n for n in line]
    print("Multiples of 3 replaced:", str(multiof3g))


for numst in linest:
    numst = numst.rstrip()
    srgwsbvsfb(int(numst))
