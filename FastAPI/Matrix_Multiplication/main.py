from fastapi import FastAPI
import addition
import subtraction
import multplication

app= FastAPI(title="Matrix Calculator")

app.include_router(addition.api_router)
app.include_router(subtraction.api_router)
app.include_router(multplication.api_router)
