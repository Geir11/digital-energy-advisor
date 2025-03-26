
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_assumptions():
    path = os.path.join("data", "assumptions.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_irradiation_data():
    path = os.path.join("data", "irradiation_by_region.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/")
def read_root():
    return {"message": "Backend is running. Ready to calculate solar energy savings!"}

@app.get("/assumptions")
def get_assumptions():
    return load_assumptions()

@app.get("/irradiation")
def get_irradiation_data():
    return load_irradiation_data()
