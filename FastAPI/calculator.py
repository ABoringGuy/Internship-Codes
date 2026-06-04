from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Numbers(BaseModel):
    a: int
    b: int
    operation: str

@app.post("/calculate")
def calculate(data:Numbers):
    if data.operation == "addition":
        return {"operation": "addition", "result": data.a + data.b}
    elif data.operation == "subtraction":
        return {"operation": "subtraction", "result": data.a - data.b}
    elif data.operation == "multiplication":
        return {"operation": "multiplication", "result": data.a * data.b}
    else:
        return {"error":" Invalid operation"}