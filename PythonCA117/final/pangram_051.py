import sys
import textwrap

text = sys.stdin.readlines()
for line in text:
    text = line.split()
    for mfin in text:
        text = [a for a in text]
    print(text.lower))