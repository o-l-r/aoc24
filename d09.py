# AOC 2024, Day 09, by OLR
from common import *

l = read_file('d09.txt')
l = l[0]

# part 1
blocks = [] # disk structure
for idx, ch in enumerate(l):
    num = int(ch)
    if idx % 2 == 0:
        blocks += [idx//2] * num # file index is idx/2: repeat 'num' times
    else:
        blocks += [-1] * num # add -1 'num' times

# [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]
#print(blocks)

while -1 in blocks:
    if blocks[-1] == -1:
        blocks.pop()
    else:
        blocks[blocks.index(-1)] = blocks.pop()
    #print(blocks)

print(sum([idx * val for idx, val in enumerate(blocks)])) # 6370402949053


# part 2
l = read_file('d09.txt')
l = l[0]

blocks = [] # disk structure

def print_blocks():
    s = ""
    for b in blocks:
        if b == -1:
            s += '.'
        else:
            s += str(b)
    print(s)

files = []
pos = 0
for idx, ch in enumerate(l):
    num = int(ch)
    if idx % 2 == 0:
        blocks += [idx//2] * num # file index is idx/2: repeat 'num' times
        files.append((idx//2, pos, num))
    else:
        blocks += [-1] * num # add -1 'num' times
    pos += num

#print(blocks)
#print(files)

def find_free_space(size):
    c = 0
    for i, v in enumerate(blocks):
        if v == -1:
            c += 1
            if c == size:
                return i - size + 1
        else:
            c = 0
    return -1

def move(idx_src, idx_dst, size):
    file = blocks[idx_src:idx_src + size]
    blocks[idx_src:idx_src + size] = [-1] * size
    blocks[idx_dst:idx_dst + size] = file

files = files[::-1] # reverse

#print_blocks()
for f in files:
    fid, pos, size = f
    dst = find_free_space(size)
    if dst != -1 and dst < pos:
        move(pos, dst, size)
    #print_blocks()

print(sum([idx * val for idx, val in enumerate(blocks) if val != -1])) # 6398096697992
