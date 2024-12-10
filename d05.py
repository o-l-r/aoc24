# AOC 2024, Day 05, by OLR
from common import *

l = read_file('d05.txt')

# test data
'''
l = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]
'''

# part1
rules = []
for line in l:
    if '|' in line:
        rules.append(tuple(line.split('|')))
updates = []
for line in l:
    if ',' in line:
        updates.append(line.split(','))
# WARNING: elements of 'rules' and 'updates' are strings, NOT int
# better solution
#rules = [x.split('|') for x in l if '|' in x]
#updates = [x.split(',') for x in l if ',' in x]

# check if all rules are satisfied
def is_valid(upd):
    for a, b in rules:
        if a in upd and b in upd:
            if upd.index(a) > upd.index(b):
                return False
    return True

s = 0
for upd in updates:
    if is_valid(upd):
        s += int(upd[len(upd)//2])
print(s)
# better solution
#valid = [upd for upd in updates if is_valid(upd)]

# part2
# WARNING: TRAP!!! there is a cycle in the provided graph/input data,
# so that it's not possible to perform the topological sort
# once and for all => we need to build a sub-graph for
# each update and perform the topological sort on it
def reorder(upd):
    g = networkx.DiGraph()
    for a,b in rules:
        if a in upd and b in upd:
            g.add_edge(a, b)
    #print(f"Is acyclic: {nx.is_directed_acyclic_graph(g)}")
    return list(networkx.topological_sort(g))

s = 0
for upd in updates:
    if not is_valid(upd):
        s += int(reorder(upd)[len(upd)//2])
print(s)
