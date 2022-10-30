import math
from statistics import *

nums_1 = sorted([4, -1, 11, 3, -5, -24])

def mean(nums):
    output = 0
    for i in nums_1:
        output += i
    return f"mean: {output/len(nums_1)}"


