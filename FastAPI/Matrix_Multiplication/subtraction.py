import numpy as np
from fastapi import APIRouter, FastAPI

from create_matrix import TwoMatrix
from validate_matrix import validate_same_shape
from validate_matrix import convert_to_numpy

api_router = APIRouter(prefix="/sub", tags=["Subtraction"])

@api_router.post("/")
def subtraction(data:TwoMatrix):
    a= convert_to_numpy(data.matrix_a)
    b= convert_to_numpy(data.matrix_b)

    validate_same_shape(a,b)
    result=np.subtract(a,b)

    return {"result":result.tolist()}