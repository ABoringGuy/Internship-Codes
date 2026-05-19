"""REDUCE Function"""
from functools import reduce

list=[1,2,3,4]

sum=reduce(lambda x, y: x+y, list)
diff=reduce(lambda x, y: x-y, list)

print(sum,diff)
"""Reduce takes values inside list to return a single value based on instruction provided."""


