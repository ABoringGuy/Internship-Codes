"""Internal working of For loops through Iterators"""

numbers=[10, 20, 30, 40]

it= iter(numbers)

while True:
    try:
        values= next(it)
        print(values)
    except StopIteration:
        break

"""Here the exception handling is done when iterator is exhausted.
With iterator, each element is processed one at a time."""

class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        print("iter() called")
        return self

    def __next__(self):
        print("next() called")

        if self.start > self.end:
            print("Iterator is exhausted")
            raise StopIteration

        value = self.start
        self.start += 1
        return value

c=Counter(1, 5)

for n in c:
    print("For Loop is called like this:", n)

"""This is how iterables are called in reality. Notice how"""