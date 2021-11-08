from typing import Optional
from pydantic import BaseModel


class Character(BaseModel):
    name: str
    age: int
    born_date: str
    concept_height: str
    gender: str
    hair_color: str
    eye_color: str
    filename: str
    appears: list[str]
    voice_actor: Optional[str] = None


class TranslatedPoem(BaseModel):
    title: str
    body: str


class Poem(BaseModel):
    title: str
    occasion: str
    body: str
    translation: Optional[TranslatedPoem]


class CharacterPoem(BaseModel):
    author: str
    poem: Poem

Poems = list[CharacterPoem]

Characters = list[Character]
