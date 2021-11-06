from fastapi import FastAPI
from .config import URL

app = FastAPI()


@app.get("/")
def root():
    return {
        "characters": f"{URL}/characters",
        "poems": f"{URL}/poems",
        "acts": f"{URL}/acts",
    }


@app.get("/characters")
def characters():
    return []


@app.get("/poems")
def poems():
    return []


@app.get("/acts")
def acts():
    return []
