# DAY 7
## What we Learned?
- Functionality of various functools
- When and why to use Cache
- How to wrap function as well as preverse wrapper functions metadata.

## Details:
- We used LRU cache if same function gets called many times.
- We used Partial to make sub-functions that share similar parameters to original function
- We used Update Wrapper to wrap functions and preserve their metadata for debugging ease.
- We used Single Dispatch to manage funciton overload
- We used CMPtoKey to easily perform operations like Compare, find Max, etc. This is done by writing a Compare function and converting it to Operational Function.
- We used Total Ordering to reduce line of code by having Python automatically detect/write non-written comparsion operators.

