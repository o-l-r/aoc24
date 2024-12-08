# AOC 2024 Day 8
from common import *

l = read_file('d08.txt')

debug = False

# Part 1

# get all antennas by frequency
d = defaultdict(list)
for y, row in enumerate(l):
    for x, car in enumerate(row):
        if car.isalnum():
            d[car].append((x, y))

# find antinodes
s = set()
for _, ant in d.items(): # for each frequency, ant = list of antennas
    for A, B in combinations(ant, 2): # for each pair of antennas
        # compute the two antinodes for pair (A, B)
        xA, yA = A[0], A[1]
        xB, yB = B[0], B[1]

        AN1 = (xB + (xB - xA), yB + (yB - yA))
        AN2 = (xA + (xA - xB), yA + (yA - yB))

        if 0 <= AN1[0] < len(l[0]) and 0 <= AN1[1] < len(l):
            s.add(AN1)
        if 0 <= AN2[0] < len(l[0]) and 0 <= AN2[1] < len(l):
            s.add(AN2)

# debug: print the map with antinodes
if debug:
    for y, row in enumerate(l):
        new_row = ""
        for x, car in enumerate(row):
            if (x, y) in s:
                new_row += "#"
            else:
                new_row += car
        print(new_row)

print(len(s)) # number of antinodes

# Part 2

s = set()
for _, ant in d.items(): # for each frequency, ant = list of antennas
    for A, B in combinations(ant, 2): # for each pair of antennas
        # compute all antinodes for pair (A, B)
        xA, yA = A[0], A[1]
        xB, yB = B[0], B[1]
        dx = xB - xA
        dy = yB - yA

        while 0 <= xA < len(l[0]) and 0 <= yA < len(l):
            s.add((xA, yA))
            xA += dx
            yA += dy

        while 0 <= xB < len(l[0]) and 0 <= yB < len(l):
            s.add((xB, yB))
            xB -= dx
            yB -= dy

# debug: print the map with antinodes
if debug:
    for y, row in enumerate(l):
        new_row = ""
        for x, car in enumerate(row):
            if (x, y) in s:
                new_row += "#"
            else:
                new_row += car
        print(new_row)

print(len(s)) # number of antinodes
