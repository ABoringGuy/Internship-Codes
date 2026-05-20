"""Note that many functions of OrderedDict has become available to Dict by Python 3.7+.
Some features like, preserving order during deletion, reinsertion, etc are done by Dict normally.
Only features not available in Dict are given below:"""

from collections import OrderedDict

"""Checking equality:"""
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od1 == od2)

d1 = {'a': 1, 'b': 2, 'c': 3}
d = {'c': 3, 'b': 2, 'a': 1}
print(d1==d)

"""As order is different, ordered dict gives false for equality.
Normal Dict gives true for equality despite positions(order) being different"""

"""Popping items:"""

d2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d3 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
res = d3.popitem(last=False)  # Remove firstinserted item
res1= d2.popitem()
print(res)
print(res1)

"""Ordered dict lets us pop either 1st or last item. Dict only allows last."""

"""Move key to end or beginning:"""

od3= OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od3)

od3.move_to_end('b')
print(od3)

od3.move_to_end('c', last=False)#Moves to front
print(od3)

"""To move to first. use move_to_end(key, last=False). There is no unique function to move to front"""

