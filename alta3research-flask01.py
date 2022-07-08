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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

herodata = [{
    "name": "EXTREMELY HANDSOME MAN",
    "realName": "Zach Lamprich",
    "since": 1995,
    "powers": [
        "really really ridiculously good looking",
        "never has been sucked into a flask",
        "Time Magazine 2006 winner",
        "+1 str, -3 int"
    ]
}]


@app.route("/")
@app.route("/start")
def start():
    return render_template("challengepage.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"):  # if nm was assigned via the POST
            return render_template("challengepage2.html")
        else:  # if a user sent a post without nm then assign value defaultuser
            flash("You entered an invalid name!", "info")
            return redirect(url_for("start"))


@app.route("/questions", methods=["POST"])
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
