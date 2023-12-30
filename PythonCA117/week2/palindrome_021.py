import sys

from string import punctuation
lis1 = sys.stdin.readlines()

for line in lis1:
    p = line.lower().strip()
    for pink in p:
        if pink in punctuation or pink == " ":
            p = p.replace(pink, "", 1)
    print(p == p[::-1])
