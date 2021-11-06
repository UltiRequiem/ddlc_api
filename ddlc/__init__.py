from fastapi import FastAPI, HTTPException

from .models import Character
from .exceptions import CharacterNotFound
from .config import URL
from .database import DBService

app = FastAPI()


@app.get("/")
async def root():
    return {
        "characters": f"{URL}/characters",
        "poems": f"{URL}/poems",
        "acts": f"{URL}/acts",
    }


@app.post("/characters")
async def create_character(character: Character):
    DBService.new_character(character.__dict__)
    return {"message": f"Character {character.name.capitalize()} added successfully."}


@app.get("/characters")
async def characters():
    return DBService.get_characters()


@app.get("/characters/{character}")
async def specific_character(character: str):
    try:
        return DBService.get_character(character)
    except CharacterNotFound:
        raise HTTPException(
            status_code=404, detail=f'Character "{character}" not found.'
        )


@app.get("/poems")
async def poems():
    return []


@app.get("/acts")
async def acts():
    return []
