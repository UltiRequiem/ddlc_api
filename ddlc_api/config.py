import os

from dotenv import load_dotenv

load_dotenv()

DEV = os.environ.get("FLASK_ENV") == "development"
URL = "http://localhost:5000" if DEV else "https://ddlcapi.herokuapp.com"

DB_USER, DB_PASSWORD, SUBDOMAIN, CLUSTER_NAME, DB_NAME = (
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("SUBDOMAIN"),
    os.environ.get("CLUSTER_NAME"),
    os.environ.get("DB_NAME"),
)
