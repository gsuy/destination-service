from typing import Optional
from fastapi import FastAPI
from controllers import predictModel
from data_structures import GridTripInfo

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World, This root page!"

@app.post("/predict")
def post_predictModel(info:GridTripInfo):
    return predictModel(info)