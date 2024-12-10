# What I've learned in Python in AOC 2024?
OLR, 12/2024

I have a lot of experience in C/C++ and many other languages, 
but I'm still a beginner in Python.
So I'm using AOC to learn Python. Here's what I found this 
year, what I found really useful and practical in Python


## Multi comparison
```python
if 1 <= a <= 3: ...
```


## Inverse/reverse a string or a list
Reverse a string
```python
s = "hello"
reversed_s = s[::-1]
```

Reverse a list
```python
l = [1, 2, 3, 4]
reversed_l = l[::-1]
```


## List Comprehension
```python
squares = [x**2 for x in range(10)]
print(squares)
```


## Counter: to create a dict to count #occurrences of each elements
```python
from collections import Counter

l = [1, 2, 1, 3, 2, 1]
dic = Counter(l)

print(dic)
print(dic[1])

# also work with str
```


## defaultdict instead of dict
defaultdict: if you access a missing key, it creates the key
with a default value provided by a default factory function.
```python
from collections import defaultdict

# Default factory is int, which returns 0
d = defaultdict(int)
print(d["missing"])  # Output: 0

# Adding to the missing key
d["missing"] += 1
print(d)  # Output: defaultdict(<class 'int'>, {'missing': 1})
```


## Useful functions on 'iterable'
```python
l = [8, 5, 7, 8, 3, 8]
print(sum(l))
print(l.count(8))
```


## List of N first integers
```python
l = list(range(n))
print(l)
l = [e for e in range(n)]
```


## all /any
```python
l = [True, True, False]
# Check if all elements are True
if all(l):
    print("All elements are True")
else:
    print("Not all elements are True")
# Check if any element is True
if any(l):
    print("At least one element is True")
else:
    print("No elements are True")
```


## Loop: enumerate to get both index and value
```python
l = [8, 5, 7]
for idx, val in enumerate(l):
    print(f"{idx}: {val}")
```


## The magic zip function
```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
for v1, v2 in zip(l1, l2):
    print(f"{v1+v2}")
```


## Powerful itertools: cartesian product / combinations / permutations
```python
from itertools

l1 = [1, 2]
l2 = ['a', 'b']
for p in product(l1, l2):
    print(p)

l = ['+', '-', '*']
for p in product(l, repeat=5):
    print(p)

l = [1, 2, 3, 4]
for c in combinations(l, 2):
    print(c)

l = [1, 2, 3]
for p in permutations(l, 2):
    print(p)
```


## Sort (sorted = create a new list)
```python
l = ['apple', 'banana', 'cherry', 'date']

# Sort by length of the string
sorted_l = sorted(l, key=len)
print(sorted_l)

# Sort by reverse alphabetical order
sorted_l = sorted(l, key=lambda x: x[::-1])
print(sorted_l)
```


## Graph
```python
import networkx

g = networkx.DiGraph()
g.add_edge(1, 2)
...
is_acyclic = networkx.is_directed_acyclic_graph(g)
list_sorted = list(networkx.topological_sort(g))

paths = networkx.descendants(g, (x,y))
for x, y in paths: ...
```
