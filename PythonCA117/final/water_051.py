import sys
liter = sys.stdin.readline()
liter = int(liter)
buckets = sys.stdin.readlines()
for line in buckets:
    buckets = line.split()
    for mfin in buckets:
        buckets = [int(a) for a in buckets]
i = -1
token = 0
for bucket in buckets:
    token = token + bucket
    i = i + 1
    if token > liter:
        break
print(i)
