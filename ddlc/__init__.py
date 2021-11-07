from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from .models import Character
from .exceptions import CharacterNotFound
from .config import URL, DEV, DEPLOY_URL
from .database import DBService

app = FastAPI()


app.mount(
    "/illustrations",
    StaticFiles(directory="assets/illustrations"),
    name="illustrations",
)


@app.get("/")
async def root():
    return {
        "characters": DBService.get_characters(),
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


@app.post("/characters")
async def create_character(character: Character):
    if not DEV:
        return {"message": "This endpoint is not available in production."}

    character_data = character.dict()
    character_data.update({"illustration": f"{DEPLOY_URL}/illustrations/{character.name}.png"})

    DBService.new_character(character_data)

    return {
        "message": f"Character {character.name.capitalize()} added successfully.",
    }


@app.get("/poems")
async def poems():
    return {
        "monika": f"{URL}/poems/monika",
        "sayori": f"{URL}/poems/sayori",
        "yuri": f"{URL}/poems/yuri",
        "natsuki": f"{URL}/poems/natsuki",
    }


@app.get("/poems/{character}")
async def character_poem(character: str):
    return {"TODO": "TODO"}
