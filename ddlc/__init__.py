from fastapi import FastAPI, HTTPException

from .models import Character
from .exceptions import CharacterNotFound
from .config import URL, DEV
from .database import DBService

app = FastAPI()


@app.get("/")
async def root():
    return {
        "characters": f"{URL}/characters",
        "poems": f"{URL}/poems",
    }


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
    return {
        "monika": f"{URL}/poems/monika",
        "sayori": f"{URL}/poems/sayori",
        "yuri": f"{URL}/poems/yuri",
        "natsuki": f"{URL}/poems/natsuki",
    }


@app.post("/characters")
async def create_character(character: Character):
    if not DEV:
        return {"message": "This endpoint is not available in production."}

    DBService.new_character(character.__dict__)

    return {
        "message": f"Character {character.name.capitalize()} added successfully.",
    }


@app.get("/poems/{character}")
async def character_poem(character: str):
    return {"TODO": "TODO"}
