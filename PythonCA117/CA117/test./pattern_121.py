import sys

pat = []
final = []
str1 = ""
t = sys.stdin.readlines()
for c in t:
    char = c.strip()
    for f in char:
        if f == "-":
            for ind in char:
                pat.append(ind)
for lower in t:
    i = 0
    match = []
    for Lchar in lower.strip():
        match.append(Lchar)
    while i < len(pat) and len(match) == len(pat):
        if match[i] == pat[i] or pat[i] == '-':
            i = i + 1
        else:
            i = 100
    if len(pat) == i and len(match) == len(pat) and match != pat:
        final.append(str1.join(match))
if len(final) > 0:
    print(*final, sep = ", ")
