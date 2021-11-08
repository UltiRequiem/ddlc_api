import pymongo

from .config import DB_PASSWORD, DB_USER, CLUSTER_NAME, SUBDOMAIN, DB_NAME

from .exceptions import CharacterNotFound


class DatabaseService:
    def __init__(self):
        client = pymongo.MongoClient(
            f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.{SUBDOMAIN}.mongodb.net/{DB_NAME}"
        )
        self.db = client[DB_NAME]

    def get_collection(self, collection_name):
        return self.db[collection_name].find({}, {"_id": False})

    def get_characters(self):
        return list(self.get_collection("characters"))

    def get_character_by_name(self, name):
        for character in self.get_characters():
            if character.name == name:
                return character

        raise CharacterNotFound()

    def new_character(self, character):
        self.db.characters.insert_one(character)


DBService = DatabaseService()
