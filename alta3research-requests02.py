import json
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask import flash
from flask import jsonify
import json


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

persondata = [{"name": "default"}]


@app.route("/")
@app.route("/start", methods=["POST"])
def start():
    return render_template("challengepage.html")


@app.route("/hint", methods=["POST"])
def hint():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(persondata)
            name = data["name"]
            persondata.append({"name": name})

            return jsonify(persondata)


@app.route("/login", methods=["POST"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"):  # if nm was assigned via the POST
            return render_template("challengepage2.html")
        else:  # if a user sent a post without nm then assign value defaultuser
            flash("You entered an invalid name!", "info")
            return redirect(url_for("start"))


@app.route("/questions", methods=["POST", "GET"])
def questions():
    accepted_answers = {"Zach", "zach", "ZACH"}
    hint_answers = {"HINT", "hint", "Hint"}
    if request.form.get("answer"):
        input_answer = request.form.get("answer")
        if input_answer in accepted_answers:
            return redirect(url_for("correct"))
        elif input_answer in hint_answers:
            return redirect("/hint")
        else:
            return render_template("challengepage2.html")


@app.route("/correct")
def correct():
    return f"Congratulations! You passed the quiz!\n"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2224)
