#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from flask import url_for
from flask import flash
from flask import jsonify
import json


app = Flask(__name__)

herodata = [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
    ]
}]


@app.route("/")
@app.route("/start", methods=["POST"])
def start():
    return render_template("challengepage.html")


@app.route("/questions", methods=["POST", "GET"])
def questions():
    accepted_answers = {"Zach", "zach", "ZACH"}
    hint_answers = {"HINT", "hint", "Hint"}
    if request.form.get("answer"):
        input_answer = request.form.get("answer")
        if input_answer in accepted_answers:
            return redirect(url_for("correct"))
        elif input_answer in hint_answers:
            return redirect("/data")
        else:
            return render_template("challengepage2.html")


@app.route("/data", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            name = data["name"]
            realName = data["realName"]
            since = data["since"]
            powers = data["powers"]
            herodata.append({"name": name, "realName": realName,
                            "since": since, "powers": powers})

    return jsonify(herodata)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
