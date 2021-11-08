import pymongo

from .config import DB_PASSWORD, DB_USER, CLUSTER_NAME, SUBDOMAIN, DB_NAME
from .exceptions import CharacterNotFound, PoemAuthorNotFound


class DatabaseService:
    def __init__(self):
        client = pymongo.MongoClient(
            f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.{SUBDOMAIN}.mongodb.net/{DB_NAME}"
        )
        self.db = client[DB_NAME]

    def get_collection(self, collection_name: str):
        return self.db[collection_name].find({}, {"_id": False})

    def get_characters(self):
        return list(self.get_collection("characters"))

    def get_character_by_name(self, name: str):
        for character in self.get_characters():
            if character["name"] == name:
                return character

        raise CharacterNotFound()

    def new_character(self, character):
        self.db.characters.insert_one(character)

    def get_poems(self):
        return list(self.get_collection("poems"))

    def get_poem_by_author(self, author):
        print(self.get_poems())
        for poem in self.get_poems():
            if poem["author"] == author:
                return poem

        raise PoemAuthorNotFound()

    def new_poem(self, poem):
        self.db.poems.insert_one(poem)


DBService = DatabaseService()
