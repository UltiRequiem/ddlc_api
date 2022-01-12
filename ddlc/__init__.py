from fastapi import FastAPI, HTTPException, staticfiles
from fastapi.middleware.cors import CORSMiddleware

from .models import Character, CharacterPoemList
from .exceptions import CharacterNotFound, PoemAuthorNotFound
from .config import DEV, DEPLOY_URL
from .database import DBService

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"characters": DBService.get_characters(), "poems": DBService.get_poems()}


@app.get("/characters")
async def characters():
    return DBService.get_characters()


@app.get("/characters/{character}")
async def specific_character(character: str):
    try:
        return DBService.get_character_by_name(character)
    except CharacterNotFound:
        raise HTTPException(
            status_code=404, detail=f'Character "{character}" not found.'
        )


@app.post("/characters")
async def create_character(character: Character):
    if not DEV:
        return {"detail": "This endpoint is not available in production."}

    character_data = character.dict()

    character_data.update(
        {"illustration": f"{DEPLOY_URL}/illustrations/{character.name}.png"}
    )

    DBService.new_character(character_data)

    return {
        "detail": f"Character {character.name.capitalize()} added successfully.",
    }


@app.get("/poems")
def poems():
    return DBService.get_poems()


@app.get("/poems/{author}")
def character_poem(author: str):
    try:
        return DBService.get_poem_by_author(author)
    except PoemAuthorNotFound:
        raise HTTPException(
            status_code=404, detail=f'Character "{author.capitalize()}" not found.'
        )


@app.post("/poems")
def create_poem(character_poems: CharacterPoemList):
    if not DEV:
        return {"detail": "This endpoint is not available in production."}

    DBService.new_poem(character_poems.dict())

    return {
        "detail": f"{character_poems.author.capitalize()} Poems added successfully.",
    }


app.mount(
    "/illustrations",
    staticfiles.StaticFiles(directory="assets/illustrations"),
    name="illustrations",
)


@app.get("/illustrations")
async def illustrations():
    return {
        "yuri": f"{DEPLOY_URL}/illustrations/yuri.png",
        "natsuki": f"{DEPLOY_URL}/illustrations/natsuki.png",
        "sayori": f"{DEPLOY_URL}/illustrations/sayori.png",
        "monika": f"{DEPLOY_URL}/illustrations/monika.png",
    }
