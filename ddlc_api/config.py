import os

DEV = os.environ.get("FLASK_ENV") == "development"
URL = "http://localhost:5000" if DEV else "https://ddlcapi.herokuapp.com"
