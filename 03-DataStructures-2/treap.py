#!/usr/bin/env python3
import sys
input = sys.stdin.buffer.readline
import random
random.seed('codeforces!!111!')


#For demo
#f = open("t0", "r")
#input = f.readline


def read_int():
    return int(input())


def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)

    
def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]
    

def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in array) + end)


class TreapNode:
    def __init__(self, key, prior):
        self.key = key
        self.prior = prior
        self._left = None
        self._right = None
        self._parent = None
        
    # T.left = T_1
    
    @property
    def left(self):
        return self._left
        
    @left.setter
    def left(self, l):
        self._left = l
        if l is not None:
            l._parent = self
            
    @property
    def right(self):
        return self._right
        
    @right.setter
    def right(self, r):
        self._right = r
        if r is not None:
            r._parent = self
            
    
    @property
    def parent(self):
        return self._parent
        
    def __str__(self):
        return f"({self.key}, {self.prior})"
        
    def _print(self):
        print(self, self.left, self.right)
        if self.left is not None:
            self.left._print()
        if self.right is not None:
            self.right._print()
        
    
class Treap:
    def __init__(self, key=None, prior=None, node_class=TreapNode):   
        self.nodes = []
        self.node_class = node_class
        if key is None:
            assert prior is None
            self.root = None
        else:
            self.root = node_class(key, prior)
            self.nodes.append(root)
            
    def insert(self, key, prior):
        node = self.node_class(key, prior)
        self.nodes.append(node)
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
            
    def _insert(self, t, node: TreapNode):
        t1, t2 = self.split(t, node.key)
        t1 = self.merge(t1, node)
        return self.merge(t1, t2)            
                
    def split(self, t, k):
        if t is None:
            return None, None
        if k > t.key:
            t1, t2 = self.split(t.right, k)
            t.right = t1
            return t, t2
        else: # k <= t.key
            t1, t2 = self.split(t.left, k)
            t.left = t2
            return t1, t
    
    def merge(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        if t1.prior > t2.prior:
            t1.right = self.merge(t1.right, t2)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2
       

class TreapNodeIndex(TreapNode):
    def __init__(self, key, val, idx):
        super().__init__(key, val)
        self.idx = idx        

class TreapIndex(Treap):
    def __init__(self, key=None, prior=None, idx=None, node_class=TreapNodeIndex):
        self.nodes = []
        self.node_class = node_class
        if key is None:
            assert prior is None
            assert idx is None
            self.root = None
        else:
            self.root = node_class(key, prior, idx)
            self.nodes.append(root)
    
    def insert(self, key, prior, idx):
        node = self.node_class(key, prior, idx)
        self.nodes.append(node)
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
        
        

n = read_int()
t = TreapIndex()
ikp = []
for idx in range(n):
    k, p = read_int_list()
    ikp.append((idx, k, p))

for idx, k, p in sorted(ikp, key=lambda _ikp: -_ikp[2]):
    t.insert(k, -p, idx)

print("YES")
for node in sorted(t.nodes, key=lambda node: node.idx):
    print(node.parent.idx + 1 if node.parent else 0,
          node.left.idx + 1 if node.left else 0,
          node.right.idx + 1 if node.right else 0)     
    #print(node, node.left, node.right, node.idx)     
        
#print("t.root._print():")        
#t.root._print()       
       
       
       
       
       
       
       
       
       
       
       
            
