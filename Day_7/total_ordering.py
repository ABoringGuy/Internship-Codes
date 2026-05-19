"""TOTAL ORDERING"""
from functools import total_ordering


@total_ordering
class comparison:

    def __init__(self,value):
        self.value = value

    def __eq__(self,other):
        return self.value == other.value

    def __lt__(self,other):
        return self.value < other.value

print("2 is less than 3", comparison(2) < comparison(3))
print("2 is equal to 2", comparison(2) ==comparison(2))
print("2 is greater than 1", comparison(2)> comparison(1))
print("2 is less than or equal to 3", comparison(2) <= comparison(3))
print("3 is greater than or equal to 2", comparison(3) >= comparison(2))

"""Here even though we didnt write function for greater than, less than/equal to functions in class,
 we are able to perform these tasks. This is because the constructor @total_ordering writes all other
 comparison functions itself. This helps reduce the length of code developer needs to write."""
