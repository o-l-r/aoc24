# AOC 2024, Day 10, by OLR
from common import *

l = read_file('d10.txt')

# part 1
# build matrix
m = []
for line in l:
    row = []
    for ch in line:
        row.append(int(ch))
    m.append(row)
#m=[[int(c) for c in r] for r in l]

R = len(m) # number of rows
C = len(m[0]) # number of columns

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

# build graph
g = networkx.DiGraph()
for x in range(R):
    for y in range(C):
        h = m[x][y]
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == h+1:
                g.add_edge((x,y),(nx,ny))
       
# count trailheads
s = 0
for x in range(R):
    for y in range(C):
        if m[x][y] == 0:
            paths = networkx.descendants(g, (x,y))
            for cx, cy in paths:
                if m[cx][cy] == 9:
                    s += 1
print(s)

# part 2
def count_paths(x, y): # count paths from (x,y) to 9 recursively
    h = m[x][y]
    if h == 9:
        return 1
    c = 0
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == h+1:
            c += count_paths(nx, ny)
    return c

s = 0
for x in range(R):
    for y in range(C):
        if m[x][y] == 0:
            s += count_paths(x, y)
# s = sum(count_paths(x, y) for x in range(R) for y in range(C) if m[x][y] == 0)
print(s)
