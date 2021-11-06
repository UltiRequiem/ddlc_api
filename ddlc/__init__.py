from fastapi import FastAPI, HTTPException

from .exceptions import CharacterNotFound
from .config import URL
from .database import DBService

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
    return DBService.get_characters()


@app.get("/characters/{character}")
def specific_character(character: str):
    try:
        return DBService.get_character(character)
    except CharacterNotFound:
        raise HTTPException(
            status_code=404, detail=f'Character "{character}" not found.'
        )


@app.get("/poems")
def poems():
    return []


@app.get("/acts")
def acts():
    return []
