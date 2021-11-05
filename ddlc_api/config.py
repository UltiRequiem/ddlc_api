import os

DEV = os.environ.get("DEV") == "true"
URL = "http://localhost:5000" if DEV else "https://ddlcapi.herokuapp.com"
