from pymongo import MongoClient

from .config import DB_PASSWORD, DB_USER, CLUSTER_NAME, SUBDOMAIN, DB_NAME

MONGO_URI = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.{SUBDOMAIN}.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

DB = client[DB_NAME]
