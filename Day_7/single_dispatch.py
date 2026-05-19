"""SINGLE DISPATCH:"""

from functools import singledispatch

@singledispatch
def process(var):
    print("Default")

@process.register(int)
def _(var):
    print(var*2)

@process.register(str)
def _(var):
    print(var)

@process.register(bool)
def _(var):
    if var:
        print("True")
    else:
        print("False")

process(10)
process("abc")
process(False)
process(True)
process(None)
"""Helps with function overload. Function overload lets us use same function name for different functions.
Define base function with @singledispatch and then put @basefunctionname.register(datatype) for using functions."""