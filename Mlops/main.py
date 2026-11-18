from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Hello! I am going to be an MLOps Engineer."}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"Message": f"Hello {name} ! Welcome to our mlops journey,"}
