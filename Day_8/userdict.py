"""Dict and other iterables are all implementation of C Language rather than Python.
Some internal operations directly manipulate the dictionary storage instead of calling Python-level overridden methods.
Below with normal Dict, our __setitem__ function gets completely bypassed."""


from collections import UserDict

class LowerDict_withDictOnly(dict):

    def __setitem__(self, key, value):
        print("Custom setitem called")
        super().__setitem__(key.lower(), value)

d = LowerDict_withDictOnly(NAME="Ram")
print(d)


"""UserDict acts like a wrapper written purely in Python. This wrapper actually wraps around a dictionary. 
UserDict actually stores data is self.data in UserDict class which can be altered by userdefined functions"""

class LowerDict_withUserDict(UserDict):

    def __setitem__(self, key, value):
        print("Custom setitem called")
        super().__setitem__(key.lower(), value)

d1 = LowerDict_withUserDict(NAME="Ram")
print(d1)