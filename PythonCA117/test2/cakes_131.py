import sys

def main():

    for line in sys.stdin:

        numbers = sorted(
            [int(t) for t in line.strip().split()], reverse=True)

        freebies = numbers[2::3]

        print(sum(numbers) - sum(freebies))


if __name__ == '__main__':
    main()
