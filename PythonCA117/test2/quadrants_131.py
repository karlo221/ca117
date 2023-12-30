import sys

def find(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)


for line in sys.stdin:
    quads = []
    line = line.split()
    quads.append(line)
    find(int(line[0]), int(line[1]))
