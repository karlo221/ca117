import sys
lines = sys.stdin.readlines()

def multiples(nums):
    r = range(1, nums + 1)
    r = list(r)
    multiof3g = [n for n in r if n % 3 == 0]
    multiof3sg = [(n ** 2) for n in r if n % 3 == 0]
    multiof4dg = [(n * 2) for n in r if n % 4 == 0]
    multiof3a4g = [n for n in r if n % 3 == 0 and n % 4 == 0]
    multiof3o4g = [n for n in r if n % 3 == 0 or n % 4 == 0]
    print("Multiples of 3:", str(multiof3g))
    print("Multiples of 3 squared:", str(multiof3sg))
    print("Multiples of 4 doubled:", str(multiof4dg))
    print("Multiples of 3 or 4:", str(multiof3o4g))
    print("Multiples of 3 and 4:", str(multiof3a4g))


for line in lines:
    line = line.strip()
    multiples(int(line))
