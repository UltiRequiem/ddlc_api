import os
import dotenv

dotenv.load_dotenv()

DEV = os.environ.get("ENV") == "dev"

DB_USER, DB_PASSWORD, SUBDOMAIN, CLUSTER_NAME, DB_NAME, URL = (
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("SUBDOMAIN"),
    os.environ.get("CLUSTER_NAME"),
    os.environ.get("DB_NAME"),
    "http://localhost:8000" if DEV else "https://ddlcapi.herokuapp.com",
)
