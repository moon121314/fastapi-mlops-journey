import sqlite3
import os
from dotenv import load_dotenv
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

load_dotenv()

DB_NAME = os.getenv("DATABASE_NAME", "predictions.db")


@app.get("/")
def read_root():
    return {"Message": "Hello! I am going to be an MLOps Engineer."}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"Message": f"Hello {name} ! Welcome to our mlops journey,"}

#define what the order form looks like
class HouseData(BaseModel):
    square_feet: float
    bedrooms: int

@app.post("/predict_price")
def predict_price(data: HouseData):
    estimated_price = (data.square_feet*150) + (data.bedrooms * 1000)

    return {
        "status":"success",
        "input_received": data,
        "predicted_price": estimated_price
    }

@app.get("/history")
def get_history():
    cursor.excute("SELECT *FROM history")

    rows = cursor.fetchall()
    histroy_list =[]

    for row in rows:
        record = {
            "id": row[0],
            "square_feet": row[1],
            "bedrooms": row[2],
            "predicted_price":row[3]
        }

        histroy_list.append(record)

    return {"history": histroy_list}
