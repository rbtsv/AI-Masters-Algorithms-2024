#!/usr/bin/env python3
import sys, os
input = sys.stdin.buffer.readline
input = lambda: sys.stdin.buffer.readline().decode('utf-8')

def create_input(test_file = "01"):
    test_file = open(f"./tests/{test_file}", "r")
    return test_file.readline


DEBUG = False
if DEBUG:
    input = create_input()


def read_int():
    return int(input())

def read_int_list():
    return [int(x) for x in input().split()]
    
INFTY = float('inf')  

class SegTreeNode:  
    def __init__(self, idx, val=INFTY):
        self.idx = idx # index in a
        self.val = val
        self.leftmost = None
        self.rightmost = None
        
    def __str__(self):
        return f"(idx={self.idx}, val={self.val})"

    def __repr__(self):
        return f"(idx={self.idx}, val={self.val})"
    

class SegTree:
    def __init__(self, inp: list):
        self.inp = inp
        self.a = []
        n = len(inp)
        m = 1 # min(power of 2) ≥ n 
        h = 0 # height of the tree
        while m < n:
            h += 1
            m *= 2
        
        self.total_length = 2**(h+1)-1
        self.a = [None] * self.total_length
        self.fst = self.total_length - m # index of first element of the input in a
        fst = self.fst
        
        for i, val in enumerate(inp):
            self.a[fst+i] = SegTreeNode(fst+i, val)
            self.a[fst+i].leftmost = i
            self.a[fst+i].rightmost = i
            
        for i in range(fst+n, self.total_length):
            self.a[i] = SegTreeNode(i, INFTY)
            self.a[i].leftmost = i
            self.a[i].rightmost = i
            
        for i in range(fst-1, -1, -1):
            left = self.a[self.left(i)]
            right = self.a[self.right(i)]
            self.a[i] = SegTreeNode(i, min(left.val, right.val))
            self.a[i].leftmost = left.leftmost
            self.a[i].rightmost = right.rightmost
            
                    
    
    def __call__(self, l, r): # l и r нумеруются с нуля как массив inp у нас в памяти      
        left_idx = l + self.fst
        right_idx = r + self.fst
        min_l, min_r = self.a[left_idx].val, self.a[right_idx].val
        
        node = self.a[left_idx]
        parent = self.a[self.parent(node.idx)]
        while parent is not None and parent.rightmost <= r:
           if self.right(parent.idx) != node.idx:
               brother = self.a[self.right(parent.idx)] 
               min_l = min(min_l, brother.val)
           node = parent
           parent = self.a[self.parent(node.idx)] if self.parent(node.idx) is not None else None
           
        node = self.a[right_idx]
        parent = self.a[self.parent(node.idx)]
        while parent is not None and parent.leftmost >= l:
           if self.left(parent.idx) != node.idx:
               brother = self.a[self.left(parent.idx)] 
               min_r = min(min_r, brother.val)
           node = parent
           parent = self.a[self.parent(node.idx)] if self.parent(node.idx) is not None else None
           
        return min(min_l, min_r)
            
    
    def parent(self, idx): # Если нумерация с единицы: parent(idx) = idx // 2
        p = (idx + 1) // 2 - 1
        return p if p >= 0 else None
        
    def left(self, idx):
        c = (idx + 1) * 2 - 1
        return c if c < len(self.a) else None
    
    def right(self, idx):
        c = (idx + 1) * 2 
        return c if c < len(self.a) else None
        
    def print_tex_subtree(self, ind, d):
        node = self.a[ind]
        self.tex_str += f"([level{d}]{{${node.val}_{{{node.idx+1}}}$}}"
        #self.tex_str += "{"+f"{node.idx+1}"+"}$}}"
        if 2*(ind+1) < self.total_length:
            self.print_tex_subtree(2*(ind+1)-1, d+1)
            self.print_tex_subtree(2*(ind+1), d+1)
        self.tex_str += ")"
        
    def print_tex(self):
        self.tex_str = ""
        self.print_tex_subtree(0, 1)
        return self.tex_str
    


#rmq = SegTree([1,3,2,4,0,7,5,6])
#os.system(f"echo '{rmq.print_tex()}' | ruby to_tree.rb")



n = read_int()
rmq = SegTree(read_int_list())
if DEBUG:
    os.system(f"echo '{rmq.print_tex()}' | ruby to_tree.rb")
for _ in range(read_int()):    
    l, r = read_int_list()
    l, r = l-1, r-1
    if DEBUG:
        print(f"==rmq({l+1},{r+1}):")
    print(rmq(l, r))
    if DEBUG:
        print("<-QUERY")