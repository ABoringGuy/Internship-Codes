import multiprocessing
import time

# A CPU-intensive function (keeps CPU busy)
def heavy_task(process_id):
    print(f"Process {process_id} started")

    total = 0
    for i in range(50_000_000):  # increase if you want more load
        total += i * i

    print(f"Process {process_id} finished")
    return total


if __name__ == "__main__":
    start_time = time.time()

    # Number of processes = number of CPU cores (or set manually)
    num_processes = 1

    processes = []

    for i in range(20):
        p = multiprocessing.Process(target=heavy_task, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    end_time = time.time()

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")