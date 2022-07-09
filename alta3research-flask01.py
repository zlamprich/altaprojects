#!/usr/bin/env python3
"""DEMO: receiving JSON"""
from flask import make_response
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
def start():
    return render_template("challengepage.html")


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            flash("Assigning 'default' as username!", "info")
            user = "default"
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
        # cookievar #value
        resp.set_cookie("userID", user)

        return resp

    if request.method == "GET":
        return redirect(url_for("start"))


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f'Welcome {name}!! Heres your stored cookie!!'


@app.route("/questions", methods=["POST", "GET"])
def questions():
    accepted_answers = {"Zach", "zach", "ZACH"}
    hint_answers = {"HINT", "hint", "Hint"}
    if request.values.get("answer"):
        input_answer = request.values.get("answer")
        if input_answer in accepted_answers:
            return redirect(url_for("correct"))
        elif input_answer in hint_answers:
            return redirect("/data")
    else:
        return render_template('challengepage2.html')


@app.route("/data", methods=["GET", "POST"])
def data():
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


@app.route("/correct")
def correct():
    return f"Congratulations! You passed the quiz!\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
