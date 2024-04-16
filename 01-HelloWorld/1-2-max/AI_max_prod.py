import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())

n = read_int()

a, b = read_int(), read_int()
m1, m2 = max(a,b), min(a,b)

for _ in range(n-2): 
    a = read_int() 
    if a >= m1: 
        m2 = m1
        m1 = a
    else:
        m2 = max(m2, a)

print(m2*m1)     