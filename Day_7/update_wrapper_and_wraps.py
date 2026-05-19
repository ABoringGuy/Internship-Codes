"""UPDATE_WRAPPER:"""
from functools import update_wrapper

def animal(dog):
    def wrapper():
        """This is an animal document"""
        print("Following is an animal:")
        dog()
    update_wrapper(wrapper, dog)
    return wrapper


def dog():
    """This is dog document"""
    print("Dog")
    return dog

dog=animal(dog)
dog()
print(f"Function name:{dog.__name__}")
print(f"Function docstring:{dog.__doc__}")


"""Here update_wrapper is used to preserve the original function(in this case dog()) metadata.
Without using update wrapper, the output would be:
Animal Function
Function name:animal
Function docstring:This is animal document
We wouldn't know that animal function is wrapped in dog function without it
dog=wrapper function
animal=wrapped function"""


"""wraps"""
from functools import wraps

def person(func):#This is a decorator function for sudyumna()
    @wraps(func)
    def wrapper():
        """This is an animal document"""
        print("Following is an person:")
        func()
    return wrapper


"""@person is equivalent to sudyumna=person(sudyumna)"""
@person
def sudyumna():
    """This is sudyumna document"""
    print("sudyumna")
    return sudyumna

sudyumna()

print(f"Function name:{sudyumna.__name__}")
print(f"Function docstring:{sudyumna.__doc__}")
