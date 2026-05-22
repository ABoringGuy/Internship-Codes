import time

# A CPU-intensive function
def heavy_task(process_id):
    print(f"Task {process_id} started")

    total = 0
    for i in range(50_000_000):
        total += i * i

    print(f"Task {process_id} finished")
    return total


if __name__ == "__main__":
    start_time = time.time()

    num_tasks = 4  # same as number of processes earlier

    results = []

    for i in range(10):
        result = heavy_task(i)   # runs sequentially (one after another)
        results.append(result)

    end_time = time.time()

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")