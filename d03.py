# AOC 2024, Day 03, by OLR
from common import *

l = read_file('d03.txt')

# Part 1
s = 0
for line in l:
    pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    for a,b in pairs:
        s += int(a)*int(b)
print(s)
# better solution
#l = ''.join(l)
#s = sum(int(a)*int(b) for a,b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', l))

# Part 2
s = 0
enabled = True
for line in l:
    tokens = re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", line)
    for t in tokens:
        #print(t)
        if t.group(0) == 'do()':
            enabled = True
        elif t.group(0) == "don't()":
            enabled = False
        elif enabled:
            #print(t)
            a = t.group(1)
            b = t.group(2)
            s += int(a) * int(b)
print(s)
