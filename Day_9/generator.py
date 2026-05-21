from time import time

def get_primes_list(start, end):
    for num in range(start,end+1):
        if num<2:
            continue
        is_prime = True
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
            if is_prime:
                yield num

start_time = time()
for value in get_primes_list(10, 10000):
    print(value)
end_time = time()
print("Time taken:",end_time - start_time)

"""Generator don't necessarily need to be faster, but rather memory efficient. As """

