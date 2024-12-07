# AOC 2024, Day 06, by OLR
from common import *

l = read_file('d06.txt')

# test data
"""
l = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]
"""

def num_steps(x=-1, y=-1):
    # create the grid
    g = [list(row) for row in l]

    # add a blocker for part #2
    # for part 1 use x=-1, y=-1 to avoid adding a blocker
    # the blocker must not be at the starting position
    if x != -1 and y != -1 and g[y][x] != '^':
        g[y][x] = '#'

    # directions: up, right, down, left
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # find the starting position
    for y, row in enumerate(g):
        if '^' in row:
            x = row.index('^')
            break

    d = 0  # initial direction is up
    
    steps = 0 # number of steps (only for part #2 to detect "infinite" loop)
    while True:
        dx, dy = dirs[d]
        # next position
        nx, ny = x + dx, y + dy
        # check boundaries
        if not (0 <= ny < len(g) and 0 <= nx < len(g[0])):
            break
        cell = g[ny][nx]
        if cell == '#':
            d = (d + 1) % 4  # turn right
        else:
            x, y = nx, ny
            g[y][x] = 'X'  # mark visited
            steps += 1
            # !!! what a disgusting idea, but it's the simplest one 
            # I've thought of in a short space of time
            if steps > 10000: # for part #2: check for "infinite" loop (assume 10000 steps is enough)
                break

    # check if the simulation has stopped because of a loop (for part #2)
    is_loop = steps > 10000
    
    # count the number of visited position, i.e. number of 'X' in the grid
    cnt = sum(row.count('X') for row in g)
    return (cnt, is_loop)

print(num_steps()[0])

# part #2
# test each position in the grid to see if it is possible to block the path
s = 0
for x in range(len(l[0])):
    for y in range(len(l)):
        # let's add a blocker at position (x, y) 
        # and see if the path becomes a loop
        if num_steps(x, y)[1]:
            s += 1
print(s)
