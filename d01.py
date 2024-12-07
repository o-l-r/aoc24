# AOC 2024, Day 01, by OLR
from common import *

lines = read_file('d01.txt')

c1, c2 = [], []
for line in lines:
    n1, n2 = map(int, line.split())
    c1.append(n1)
    c2.append(n2)
# better solution
# c1, c2 = map(list, zip(*(map(int, line.split()) for line in read_file('d01.txt'))))

# Part 1
c1.sort()
c2.sort()
s = 0
for n1, n2 in zip(c1, c2):
    s += abs(n1 - n2)
print(s)
# better solution
#sum_diff = sum(abs(n1 - n2) for n1, n2 in zip(sorted(c1), sorted(c2)))

# Part 2
counter_c2 = Counter(c2)
score = 0
for num in c1:
    score += num * counter_c2[num]
print(score)
#score = sum(num * Counter(c2)[num] for num in c1)
