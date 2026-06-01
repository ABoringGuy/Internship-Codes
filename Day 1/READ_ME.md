# Day 1
## What we learned?
- Diamond Problem Handling in Python
- AST Tree. How it is viewed for Python and why it is used.
- MRO and how it handles inheritance parameters.
- super() and it's use for inheritance

## Details:
### AST:
- Abstract Syntax Tree(AST) represents structure of Programming Language in tree-like structure.
- It abstracts the details of syntax making it less syntax focused to understand structure of code.
- It works as:
   - Convert .py file to Bytecode(.pyc file)
   - Perform Lexical Analysis to get Tokens. 
   <img width="950" height="617" alt="image" src="https://github.com/user-attachments/assets/beacbf3d-31c1-4d42-a515-0254a5cf1277" />
   - Partse the data to proper AST Structure.
<img width="508" height="353" alt="image" src="https://github.com/user-attachments/assets/0ba253bd-5f56-4d69-b66e-63c492299095" />
<img width="756" height="781" alt="image" src="https://github.com/user-attachments/assets/bc31ad3d-3381-465b-8b60-0c34c3225717" />
<img width="946" height="590" alt="image" src="https://github.com/user-attachments/assets/b0eb371f-2bcb-441e-a9b1-bfea25c0c8e6" />

### Inheritance:
- During Inheritance, the child Class can utilize the Parent Class functions and values as if own.
- Sometimes if Parent and Child have same function name, Python may not know which function to call, causing ambiguity.
- Python automatically applies MRO to fix this issue.
  <img width="975" height="558" alt="image" src="https://github.com/user-attachments/assets/6dda27ab-f954-4651-be7a-85f1d643b44c" />
- Here we can see, MRO fixes ambiguity by calling the function of the Parent Class first in parameter of Child Class.
- Similarly, we can use .mro() to print order of MRO.
- If we want to inherit from specified class with more control, we use .super() as below.
  <img width="569" height="988" alt="image" src="https://github.com/user-attachments/assets/29e742c4-3f02-4020-b75f-b8db8c1bbd00" />

  
