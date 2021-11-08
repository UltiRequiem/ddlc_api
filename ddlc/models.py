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


PoemList = list[Poem]


class CharacterPoemList(BaseModel):
    author: str
    act_1: PoemList
    act_2: Optional[PoemList]
    act_3: Optional[PoemList]
