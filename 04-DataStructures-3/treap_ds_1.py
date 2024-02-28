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
        self.num_of_nodes = 1
        self.data = None
    
    def update_data(self):
        self.num_of_nodes = sum(node.num_of_nodes for node in self.children) + 1
        
    @property
    def children(self):
        if self.left:
            yield self.left
        if self.right:
            yield self.right
        
    def find(self, key):
        if self.key == key:
            return self
        if key > self.key and self.right is not None:
            return self.right.find(key)
        if key < self.key and self.left is not None:
            return self.left.find(key)
        return None
        
    @property
    def min(self):
        cur_min = self
        while cur_min.left is not None:
            cur_min = cur_min.left
        return cur_min
        
    @property
    def max(self):
        cur_max = self
        while cur_max.right is not None:
            cur_max = cur_max.right
        return cur_max
        
    @property
    def is_left_child(self):
        if self.parent is None:
            return None
        return self.parent.left == self
    
    @property
    def is_right_child(self):
        if self.parent is None:
            return None
        return self.parent.right == self
        
    @property
    def next(self):
        if self.right:
            return self.right.min
        
        answ = self
        while answ is not None and answ.is_right_child:
            answ = answ.parent
                
        if answ and answ.is_left_child:
            return answ.parent
        return None
        
        
    @property
    def prev(self):        
        if self.left:
            return self.left.max
    
        answ = self
        while answ is not None and answ.is_left_child:
            answ = answ.parent
            
        if answ and answ.is_right_child:
            return answ.parent
        return None
    
    
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
            
            
class TreapIter:
    def __init__(self, treap, cur_node=None):
        self.treap = treap
        self.cur_node = cur_node
        if cur_node is None:
            if self.treap:
                self.cur_node = self.treap.root.min  
                
    def __iter__(self):
        return self
        
    def __next__(self): 
        if self.cur_node is None:
            raise StopIteration 
        # return cur_node++
        cur_node = self.cur_node
        self.cur_node = cur_node.next
        return cur_node            
        
    
class Treap:
    def __init__(self, key=None, prior=None, node_class=TreapNode):   
        self.node_class = node_class
        if key is None:
            assert prior is None
            self.root = None
        else:
            self.root = node_class(key, prior) 
            
    def __len__(self):
        if self.root is None:
            return 0
        return self.root.num_of_nodes
    
    def __iter__(self):
        return TreapIter(self)
            
    def __bool__(self):
        return self.root is not None  
            
    def __contains__(self, key): # key in t -> True/False
        if self.root is None:
            return False
        return self.root.find(key) is not None
            
    def upper_bound(self, key):
        if self.root is None:
            return None
        
        t1, t2 = self.split(self.root, key)
        if t2 is None:
            return None
        answ = t2.min
        self.root = self.merge(t1, t2)
        return answ
        
    def remove(self, key):
        assert self.root is not None and key in self
        
        t1, t2 = self.split(self.root, key)
        node = t2.min

        if node.parent is not None:
            node.parent.left = node.right
            self.root = self.merge(t1, t2)        
        else:
            self.root = self.merge(t1, t2.right)        

        if self.root:
            self.root._parent = None
        
            
    def insert(self, key, prior):
        node = self.node_class(key, prior)        
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
            t.update_data()
            return t, t2
        else: # k <= t.key
            t1, t2 = self.split(t.left, k)
            t.left = t2
            t.update_data()
            return t1, t
    
    def merge(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        if t1.prior > t2.prior:
            t1.right = self.merge(t1.right, t2)
            t1.update_data()
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            t2.update_data()
            return t2
       

class TreapNodeDS(TreapNode):
    def __init__(self, key, val=None):
        super().__init__(key, random.random())
        self.val = val    
    
    def __str__(self): # print(TreapNodeDs(...)), str(TreapNodeDS(...)) -> str
        return f"({self.key}, {self.val})"


class TreapNodeRMQ(TreapNodeDS):        
    def __init__(self, key, val):
        super().__init__(key, val)
        self.min_val = val
    
    def update_data(self):
        super().update_data()
        self.min_val = min([child.min_val for child in self.children] + [self.val])

class TreapDS(Treap):
    def __init__(self, key=None, val=None, treap_node_class=TreapNodeDS):
        self.node_class = treap_node_class
        if key is None:
            assert val is None
            self.root = None
        else:
            self.root = self.treap_node_class(key, val)            
            
    def insert(self, key, val):
        node = self.node_class(key, val)        
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
                   
    def find(self, key):
        if self.root is None:
            return None
        return self.root.find(key)
            
    def __getitem__(self, key): # t[key] -> val        
        node = self.find(key)
        if node is None:
            raise Exception(f"Key {key} is not in the container")
        return node.val
    
    def __setitem__(self, key, val): # t[key] = val        
        node = self.find(key)
        if node is not None:
            node.val = val
        else:
            self.insert(key, val)
        
      
        
t = TreapDS(treap_node_class=TreapNodeRMQ)

print(f"{len(t)=}") 

t[1] = "a"

print(f"{len(t)=}, {t.root.min_val=}") 
t.remove(1)
print(f"{len(t)=}")

t[1] = "aa"
t[2] = "b"
print(f"{len(t)=}, {t.root.min_val=}") 
t[10] = "c"
print(f"{len(t)=}, {t.root.min_val=}") 
print(t[1], t[2], t[10])

# t[11]
t.remove(2)
print(f"{len(t)=}, {t.root.min_val=}") 

print(t.upper_bound(1), t.upper_bound(2), t.upper_bound(3), t.upper_bound(11))

t[2] = "bb"

print(t.find(1).next.next.prev.prev)   
      
print("=== Iterator Test ==")   

print("first:", next(iter(t)))

     
for node in t:
    print(node)                
    for _node in TreapIter(t, node):
        print("->", _node)
    for _node in iter(t):
        print("-->", _node)
    
        
        
        

  
       
       
       
       
       
       
       
       
       
       
       
            
