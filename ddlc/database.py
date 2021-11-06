import pymongo

from .config import DB_PASSWORD, DB_USER, CLUSTER_NAME, SUBDOMAIN, DB_NAME

from .exceptions import CharacterNotFound


class DatabaseService:
    def __init__(self):
        client = pymongo.MongoClient(
            f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.{SUBDOMAIN}.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
        )
        self.db = client[DB_NAME]

    def get_collection(self, collection_name):
        return self.db[collection_name].find({}, {"_id": False})

    def get_characters(self):
        return list(self.get_collection("characters"))

    def get_character(self, name):
        for character in self.get_collection("characters"):
            if character["name"] == name:
                return character

        raise CharacterNotFound()


DBService = DatabaseService()
