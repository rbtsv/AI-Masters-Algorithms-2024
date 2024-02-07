import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())

n = read_int()

for _ in range(n):
    a, b = [int(x) for x in input().split()]
    print(a+b)
    sys.stdout.flush()
