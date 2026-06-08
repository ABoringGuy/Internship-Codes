import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr.copy()

arr = [random.randint(1, 100) for _ in range(20)]

fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr)

plt.show()