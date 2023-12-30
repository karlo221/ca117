import sys

import string
gettys = sys.stdin.readlines()
unique = []

for line in gettys:
    g = line.strip().split()
    for char in g:
        char = char.lower()
        for funk in char:
            if funk in string.punctuation:
                char = char.replace(funk, "", 1)

        if char not in unique and len(char) > 0:
            unique.append(char)

print(len(unique))
