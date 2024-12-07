# AOC 2024, Day 02, by OLR
from common import *

lines = read_file('d02.txt')

# Part 1
s = 0
for line in lines:
    nums = list(map(int, line.split()))
    inc = True
    for i in range(len(nums) - 1):
        if not (1 <= nums[i+1] - nums[i] <= 3):
            inc = False
            break
    dec = True
    for i in range(len(nums) - 1):
        if not (1 <= nums[i] - nums[i+1] <= 3):
            dec = False
            break
    if inc or dec:
        s += 1
print(s)

# Part 2
def is_valid(nums):
    inc = all(1 <= nums[i+1] - nums[i] <= 3 for i in range(len(nums) - 1))
    dec = all(1 <= nums[i] - nums[i+1] <= 3 for i in range(len(nums) - 1))
    return inc or dec

s = 0
for line in lines:
    nums = list(map(int, line.split()))
    if is_valid(nums):
        s += 1
        continue
    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        #print(temp)
        if is_valid(temp):
            s += 1
            break
print(s)
