import os
import dotenv

dotenv.load_dotenv()

DEV = os.environ.get("ENV") == "dev"

DB_USER, DB_PASSWORD, SUBDOMAIN, CLUSTER_NAME, DB_NAME, DEPLOY_URL = [
    os.environ.get(x)
    for x in [
        "DB_USER",
        "DB_PASSWORD",
        "SUBDOMAIN",
        "CLUSTER_NAME",
        "DB_NAME",
        "DEPLOY_URL",
    ]
]
