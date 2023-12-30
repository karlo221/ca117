import sys

text = sys.stdin.readlines()
for line in text:
    text = line.split()
    for mfin in text:
        text = [int(a) for a in text]
number = text[0]
rooms = text[1:]
brange = [int(a) for a in range(1, number + 1)]
vacaint = []
for a in brange:
    if a not in rooms:
        vacaint.append(a)
vacaint.sort()
if len(vacaint) > 1:
    print(map(str, vacaint[:1]))
else:
    print("no room")
