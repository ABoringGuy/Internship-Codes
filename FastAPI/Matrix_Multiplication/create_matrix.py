from pydantic import BaseModel
from fastapi import FastAPI

class TwoMatrix(BaseModel):
    matrix_a: list[list[float]]
    matrix_b: list[list[float]]

class OneMatrix(BaseModel):
    matrix: list[list[float]]