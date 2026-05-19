from asyncio.windows_events import NULL
from functools import partial, partialmethod, update_wrapper

"""Partial class showcase:"""
def power(x,n):
    print(f"{x} to the power of {n} is {x**n}")

square=partial(power, n=2)
cube=partial(power, n=3)

power(4,6)
square(4)
cube(4)

"""Partial class allows us to create specified functions from existing functions.
Here, square() and cube() are Partial Class of power()"""

"""Partial Funciton/Method Class showcase"""

class Demo:
    def __init__(self,x,n):
        self.x = x
        self.n = n
        print(f"In class: {x} to the power of {n} is {x**n}")

    square=partialmethod(__init__, n=2)
    cube=partialmethod(__init__, n=3)

obj=Demo(4,4)
obj.square(4)
obj.cube(4)

"""Identical to Partial Class. It helps set arguments for class functions without affecting the function directly"""









