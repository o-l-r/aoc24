# AOC 2024, Day 04, by OLR
from common import *

l = read_file('d04.txt')

"""
l = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]
print(l)
"""

# part1
n = len(l)
m = len(l[0])
dir = [ (1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1) ]
s = 0
for x in range(n):
    for y in range(m):
        for dx, dy in dir:
            final_x = x + 3*dx
            final_y = y + 3*dy
            if 0 <= final_x < n and 0 <= final_y < m:
                seq = l[x][y] + l[x + dx][y + dy] + l[x + 2*dx][y + 2*dy] + l[final_x][final_y]
                if seq == "XMAS":
                    s += 1
print(s)
"""
# super compact solution
s = sum(
    ''.join(l[x + k*dx][y + k*dy] for k in range(4)) == word
    for x in range(n)
    for y in range(m)
    for dx, dy in directions
    if 0 <= x + 3*dx < n and 0 <= y + 3*dy < m
)
"""

# part2
s = 0
for x in range(n - 2):
    for y in range(m - 2):
        diag1 = l[x][y] + l[x+1][y+1] + l[x+2][y+2]
        diag2 = l[x][y+2] + l[x+1][y+1] + l[x+2][y]
        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            s += 1
print(s)
"""
# super compact solution
patterns = {"MAS", "SAM"}
count = sum(
    (l[x][y] + l[x+1][y+1] + l[x+2][y+2] in patterns) and
    (l[x][y+2] + l[x+1][y+1] + l[x+2][y] in patterns)
    for x in range(n - 2)
    for y in range(m - 2)
)
"""
