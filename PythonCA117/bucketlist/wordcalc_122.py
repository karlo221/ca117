#!/usr/bin/env python3

import sys
from this import s

lines = sys.stdin

oled = {}
oled_reverse = {}
for line in lines:
    line = line.strip().split()
    try:
        if line[0] == "def":
            oled[line[1]] = int(line[2])
            oled_reverse[int(line[2])] = line[1]
            for (t, y) in (oled_reverse.items()):
                t = int(t)
            for (tv, vt) in (oled.items()):
                vt = int(vt)
        if line[0] == "calc":
            calc = line[1:]
            j = 0
            to = oled[calc[0]]
            while j < len(calc):
    except IndexError
        pass

