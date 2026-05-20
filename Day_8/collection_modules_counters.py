from collections import Counter

list=["apple", "bada apple", "chota apple", "duo apple", "ek aur apple", "apple", "bada apple", "chota apple"]
dict={"apple":1,"bada apple":2,"chota apple":3, "duo apple": 1, "ek aur apple": 2}
tuple=("apple", "bada apple", "chota apple", "duo apple", "ek aur apple", "apple", "bada apple", "chota apple")
print(Counter(list))
print(Counter(dict))
print(Counter(tuple))
"""Counter simply returns the counts of element in an iterable.
As set() only supports 1 element with same name, count wont do anything for it.
The returned count is stored as Dict."""