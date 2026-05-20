from collections import ChainMap

d1={"a":"apple","b":"banana"}
d2={"c":"cherry","d":"dog"}

c=ChainMap(d1,d2)#We can chain as many dict as we want
print(c)

print(list(c.keys()))
print(list(c.values()))
print(c.maps)

"""c.maps gives list of dict. print(c) is object representation of ChainMap """

d3={"e":"elephant","f":"fox"}
c1=c.new_child(d3)
print(c1.maps)
"""new_child is used to append new dict on chainmap"""

c3=reversed(c1.maps)
print(type(c3))#Note how reversed actually returns a reverseiterator. Not list or ChainMap
print(list(c3))

"""reversed is used to reverse a chainmap. As reversed() returns a reverseiterator, we need to convert it to list to print.
Also as the datatype is a iterator, it gets exhausted after use."""