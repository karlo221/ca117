import sys
sys.stdout = open('Pyhton/output.txt', 'w')
sys.stdin = open('Pyhton/input.txt', 'r')

n, q = map(int, input().split())

print(n)
