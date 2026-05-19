"""LRU_CACHE:"""
import time
from functools import lru_cache

def square_no_cache(x):
    time.sleep(0.1)
    return (x**2)

@lru_cache(maxsize= 3)
def square_cache(x):
    time.sleep(0.1)
    return x**2

start1=time.time()
square_no_cache(2)
square_no_cache(3)
square_no_cache(2)
square_no_cache(4)
square_no_cache(5)
end1=time.time()

print("Time without cache:", end1-start1)

start=time.time()
square_cache(2)
square_cache(3)
square_cache(2)
square_cache(4)
square_cache(5)
end=time.time()

print("Time with cache:", end-start)
print(square_cache.cache_info())

"""Helps make operation of function faster by caching. Here we specified that maxsize of cache is 3. So cache list becomes as:
[2]
[2,3]
[2,3] as 2 is here, it get hit
[2,3,4]
[2,5,4] as 3 was LRU"""