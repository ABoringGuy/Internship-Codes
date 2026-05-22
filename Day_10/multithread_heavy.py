import threading
import time

def heavy_task(thread_id):
    print(f"Thread {thread_id} started")

    total = 0
    for i in range(50_000_000):
        total += i * i

    print(f"Thread {thread_id} finished")
    return total


if __name__ == "__main__":
    start_time = time.time()

    num_threads = 4
    threads = []

    for i in range(10):
        t = threading.Thread(target=heavy_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")