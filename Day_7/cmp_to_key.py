"""cmp_to_key showcase:"""
from functools import cmp_to_key

def compare_numbers(a,b):
    if a%2==0 and b%2!=0:
        return -1
    if a%2!=0 and b%2==0:
        return 1

    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

l1=[1, 5, 6, 2, 11, 9, 90, 16]
sorted_numbers = sorted(l1)
print("Sorted Numbers:", sorted_numbers)
sorted_numbers= sorted(l1, key=cmp_to_key(compare_numbers))
print("Sorted Numbers with cmp_to_key is:", sorted_numbers)

"""The function compare_numbers() simply compares 2 numbers. sorted() is a in-built function that sorts numbers in ascending order.
If we want  order to sorted in specified order, we need to usually write new functions.
Here we want to sort numbers as: Even first and Odd last but in ascending order.
In compare_nunmbers(), we simply compared very number with one another.
Using key=cmp_to_key(compare_numbers), we were able to sort those compared number.
Basically: if -1 is returned then put first, 1 put last and 0 don't change position."""



words = ["apple", "kiwi", "banana", "fig"]


def compare(a, b):

    # shorter word first
    if len(a) < len(b):
        return -1

    if len(a) > len(b):
        return 1

    return 0

result=sorted(words)
print("Without cmp_to_key: ",result)
result = sorted(words, key=cmp_to_key(compare))
print("With cmp_to_key:", result)

"""Here, if we don't use cmp_to_key(), the string does not get sorted based on length. In simplest terms,
 cmp_to_key turns a function that compares data into a function that perform operation."""