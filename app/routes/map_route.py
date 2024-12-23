from flask import render_template, request, jsonify, Blueprint, send_file
import os

from app.services.queries_service import select_query

map_blueprint = Blueprint('map', __name__)

MAPS_DIR = os.path.join(os.getcwd(),"static", "maps")


@map_blueprint.route("/", methods=["GET", "POST"])
def home():
    region = request.form.get("region", "")
    query = request.form.get("query", "home")
    if request.method == "POST":
        select_query(query, region)
    return render_template("index.html", map_file=f"/render_map/{query}")

@map_blueprint.route("/render_map/<query>")
def render_map(query):
    map_file = os.path.join(MAPS_DIR, f"{query}.html")
    if not os.path.exists(map_file):
        map_file = os.path.join(MAPS_DIR, "home.html")
    return send_file(map_file)