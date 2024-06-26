#!/Users/rubtsov/miniconda3/bin/python3
import sys
import numpy as np
input = sys.stdin.buffer.readline


#For demo
f = open("./tests/1", "r")
input = f.readline


def read_int():
    return int(input())

def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)
    
def read_int_array(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]

import numpy as np
from itertools import product

N = 1
P = 0

n = read_int()
R = read_int()
m = read_int()
Moves = set()
for _ in range(m):    
    Moves.add(tuple(read_int_array()))
        
    
Field = np.zeros((n+1,n+1), dtype=int) # 0 —> P, 1 —> N, 2 —> Not computed
Field.fill(2)

for x in range(n+1):
    y = 0
    while x*x + y*y < R*R:
        y += 1
    Field[x] = np.array([2]*(y) + [P]*(n+1-y))

Nline = np.array([1]*(n+1), dtype=int)
for x in range(n,-1,-1): 
    line = Field[x]          
    for (xx, yy) in Moves:
        X = x+xx
        if X <= n:            
            newline= Nline+np.concatenate((Field[X][yy:],
                                          np.array([2]*yy, 
                                          dtype=int)))
            line = np.min((line,  newline), axis=0)
    Field[x] = line % 2
            


print(np.flipud(Field.transpose()))
print(1 if Field[0,0] else 2)
        
            
    