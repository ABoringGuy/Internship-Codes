# Day 10
## What we Learned?
- The differnce between Thread and Process
- The difference between Multiprocessing and Multithreading
- The flow of program that implement Multiprocessing and Multithreading
- The impact of CPU Cores when using Multiprocessing(Use Resource Manger to check how CPU Cores are utilized)
- Race condition during Multithreading

## Details:
### Running Single Core Program:
<img width="721" height="865" alt="image" src="https://github.com/user-attachments/assets/1bdf74e7-18b2-41cd-a150-675e1aeee62f" />

### Running Multi-Processing Program
<img width="711" height="880" alt="image" src="https://github.com/user-attachments/assets/d10858f5-efa6-4e1a-bfee-2eecb267de1f" />

### Race condition during Multi-Threading
<img width="356" height="746" alt="image" src="https://github.com/user-attachments/assets/7ec03da8-bdf0-4527-9cce-0e248fdae96a" />

  - As we can see above, Thread 1 and Thread 2 both share a resource 'count'. Thread-1 counted till 22 and then Thread-2 took over. However as Thread-1 still holds the resource, when Thread-1 turns come, it resumes count from 23 rather than 30(where Thread-2 left).
