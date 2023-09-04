from flask import Flask, send_file, Blueprint
from flask_cors import CORS, cross_origin
from flask import jsonify, json


blueprint_api_documentation = Blueprint("api_documentation", __name__, url_prefix="")


def swagger():
    with open("swagger.json", "r") as f:
        return jsonify(json.load(f))
