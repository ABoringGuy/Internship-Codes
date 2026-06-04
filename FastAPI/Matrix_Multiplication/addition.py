from fastapi import APIRouter, FastAPI
import numpy as np

from validate_matrix import convert_to_numpy
from create_matrix import TwoMatrix
from validate_matrix import validate_same_shape

api_router = APIRouter(prefix="/add", tags=["Addition"])

@api_router.post("/")
def add(data:TwoMatrix):
    a= convert_to_numpy(data.matrix_a)
    b= convert_to_numpy(data.matrix_b)

    validate_same_shape(a,b)
    result= np.add(a,b)

    return {"result":result.tolist()}


