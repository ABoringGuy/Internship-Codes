import numpy as np
from fastapi import HTTPException, FastAPI

def convert_to_numpy(matrix):
    return np.array(matrix)

def validate_same_shape(a,b):
    if a.shape!=b.shape:
        raise HTTPException(status_code=400, detail="Matrix dimensions do not match")

def validate_multiplication(a,b):
    if a.shape[1] != b.shape[0]:
        raise HTTPException(status_code=400, detail="Matrix dimensions do not match")
