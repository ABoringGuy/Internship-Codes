"""Why outputs like T1T2 together are occurring?
print() may look like a single operation but it actually involves operation as:
1) Convert object to string
2) Write bytes to stdout buffer
3) Flush output
4) Return control

During these operations:
1) Python may release GIL
2) OS scheduler may switch threads
3) output buffer may interleave text"""


import threading
import time
counter=0
t1text="T1"
t2text="T2"

"""Uncomment to prevent race condition"""
# lock=threading.Lock()

def increment(datas:str):
    global counter
    for _ in range(60):
        # with lock:
        #     temp = counter
        #     time.sleep(0)
        #     counter = temp + 1
        #     print(f' Thread {datas}: {counter},')
        #
        temp=counter
        time.sleep(0)
        counter=temp +1
        print(f' Thread {datas}: {counter},')

"""If we end up doing this: t1= threading.Thread(target=increment(t1text)
then thread does not get initilized. We need to initialize thread as below.
Note that we pass args with comma because we pass it as tuple with single value."""

t1= threading.Thread(target=increment, args=(t1text,))
t2= threading.Thread(target=increment, args=(t2text,))

t1.start()
t2.start()

"""join() ensure any operations below it in sequence aren't executed before the thread.
If we don't write .join() below then:
print("Final value of counter: ", counter) may run before the threads complete their tasks"""

t1.join()
t2.join()

print("Final value of counter: ", counter)