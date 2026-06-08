import numpy as np
from fastapi import APIRouter, FastAPI

from create_matrix import TwoMatrix
from validate_matrix import validate_multiplication
from validate_matrix import convert_to_numpy

api_router = APIRouter(prefix="/mul", tags=["Multiplication"])

@api_router.post("/")
def multiplication(data:TwoMatrix):
    a= convert_to_numpy(data.matrix_a)
    b= convert_to_numpy(data.matrix_b)

    validate_multiplication(a,b)
    result=np.matmul(a,b)

    return {"result":result.tolist()}