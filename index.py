# main.py - FastAPI
from fastapi import FastAPI

# flask_app.py - Flask
from flask import Flask


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@flask_app.route("/")
def hello():
    return "Hello from Flask!"

if __name__ == "__main__":
    from multiprocessing import Process
