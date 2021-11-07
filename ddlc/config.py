import os
import dotenv

dotenv.load_dotenv()

DEV = os.environ.get("ENV") == "dev"

DEPLOY_URL = "https://ddlcapi.herokuapp.com"

URL = "http://localhost:8000" if DEV else DEPLOY_URL

DB_USER, DB_PASSWORD, SUBDOMAIN, CLUSTER_NAME, DB_NAME = [
    os.environ.get(x)
    for x in ["DB_USER", "DB_PASSWORD", "SUBDOMAIN", "CLUSTER_NAME", "DB_NAME"]
]
