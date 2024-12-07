# common.py

# My favorite Python imports for Advent of Code puzzles
import string
import math
from datetime import datetime
import os
import sys
import re
from math import gcd
from functools import reduce, lru_cache
from collections import defaultdict, Counter, deque  # Advanced data structures
from queue import Queue  # Queue data structure for BFS and other algorithms
import heapq  # Heap queue algorithms, useful for priority queues
from itertools import * # Powerfull iterator functions e.g. cartesian product, permutations, combinations
import pprint  # Pretty-printing data structures

# Optional: External Libraries (install via pip if needed)
import numpy as np  # Numerical operations
import pandas as pd  # Data manipulation and analysis
import networkx as nx  # Graph operations

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().strip().split('\n')

def read_lists_of_numbers(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, re.findall(r'-?\d+', line))) for line in file]

def extract_numbers(line):
    return list(map(int, re.findall(r'-?\d+', line)))
