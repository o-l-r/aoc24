# AOC 2024, Day 07, by OLR
from common import *

l = read_file('d07.txt')

# 2 diffetent solutions for part 1 and 2
# first one is recursive (the one I thought at first), 
# second one is iterativecand use cartesian product 
# to generate all possible combinations of operators

# part 1: recursive solution
def is_valid1(t, a, l):
    if len(l) == 0:
        return a == t
    return is_valid1(t, a + l[0], l[1:]) or is_valid1(t, a * l[0], l[1:])
    
s = 0
for line in l:
    t, nums = line.split(': ')
    t = int(t)
    n = list(map(int, nums.split(' ')))
    if is_valid1(t, n[0], n[1:]):
        s += t
print(s)

# part 2
def is_valid2(t, a, l):
    if len(l) == 0:
        return a == t
    return is_valid2(t, a + l[0], l[1:]) or is_valid2(t, a * l[0], l[1:]) or is_valid2(t, int(str(a) + str(l[0])), l[1:])

s = 0
for line in l:
    t, nums = line.split(': ')
    t = int(t)
    n = list(map(int, nums.split(' ')))
    if is_valid2(t, n[0], n[1:]):
        s += t
print(s)

"""
tl = [1, 2, 3]
print("Cartesian product")
for e in product(tl, repeat=2):
    print(e)
print("Permutations")
for e in permutations(tl, 2):
    print(e)
print("Combinations")
for e in combinations(tl, 2):
    print(e)
"""

# part 1
s = 0
for line in l:
    t, nums = line.split(': ')
    t = int(t)
    n = list(map(int, nums.split(' ')))
    # here is the magic!
    # generate all combinations of operators of length len(n)-1 (cartesian product)
    for ops in product(['+', '*'], repeat=len(n)-1):
        #print(ops)
        res = n[0]
        for idx, val in enumerate(n[1:]): #for val, op in zip(n[1:], ops):
            op = ops[idx]
            if op == '+':
                res += val
            else:
                res *= val
        if res == t:
            s += t
            break
print(s)

# part 2
s = 0
for line in l:
    t, nums = line.split(': ')
    t = int(t)
    n = list(map(int, nums.split(' ')))
    # generate all combinations of operators of length len(n)-1 (cartesian product)
    for ops in product(['+', '*', '||'], repeat=len(n)-1):
        #print(ops)
        res = n[0]
        for idx, val in enumerate(n[1:]): #for val, op in zip(n[1:], ops):
            op = ops[idx]
            if op == '+':
                res += val
            elif op == '*':
                res *= val
            else: # op == '||'
                res = int(str(res) + str(val))
        if res == t:
            s += t
            break
print(s)
