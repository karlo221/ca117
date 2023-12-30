import sys
linest = sys.stdin.readlines()

for line in linest:
    helosd = line.strip()
    helosd = int(helosd)
    yolol = []
    for num in range(0, helosd + 1):
        if num > 1:
            r = range(2, num)
            for i in r:
                if (num % i) == 0:
                    break
            else:
                yolol.append(num)
    print("Primes:", yolol)
