from collections import deque

d1=deque(["banana", "cucumber"])
print(d1)

d1.append("dates")
print(d1)

d1.appendleft("apple")
print(d1)

d1.extend(["eggplant", "fig", "grape"])
print(d1)

d1.extendleft(["zucchini", "yam", "ximernia", "watermelon", "vanilla beans", "ugni", "apple", "apple"])
print(d1)

d1.pop()
print(d1)

d1.popleft()
print(d1)

print(d1.count("apple"))

d1.rotate(1)
print(d1)
"""Rotate right to left by 1 element"""

d1.rotate(-1)
print(d1)
"""Rotate left to right by 1 element"""
d1.reverse()
print(d1)

d1.remove("apple")
"""Removes only the 1st instance of apple"""