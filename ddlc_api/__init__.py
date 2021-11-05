import flask

from .config import DEV, URL
from .db import DB

app = flask.Flask(__name__)

if DEV:
    app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def root():
    return {
        "characters": f"{URL}/characters",
        "poems": f"{URL}/poems",
        "acts": f"{URL}/acts",
    }


@app.route("/characters", methods=["GET"])
def characters():
    return {"characters": []}


@app.route("/poems", methods=["GET"])
def poems():
    return {"poems": []}


@app.route("/acts", methods=["GET"])
def acts():
    return {"acts": []}
