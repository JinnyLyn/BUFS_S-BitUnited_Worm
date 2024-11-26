import os
from flask import Flask, request, render_template, redirect, abort
from markupsafe import escape
from datetime import datetime
from db import read_data, write_data
PATH = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
@app.route("/board", methods=["GET"])
def board():
    posts = read_data()
    return render_template("board.html", posts=posts)


@app.route("/view", methods=["GET"])
def view():
    posts = read_data()
    idx = int(request.args.get("idx").strip())-1

    if posts[idx]["secret"] and request.remote_addr != "127.0.0.1":
        return redirect("/board")

    return render_template("view.html", post=posts[idx])


@app.route("/write", methods=["GET", "POST"])
def write():

    if request.method == "GET":
        return render_template("write.html")
    else:
        subject = request.form.get("subject")
        author = request.form.get("author")
        body = escape(request.form.get("body"))
        date = request.form.get("date")
        secret = True if request.form.get("secret", "off") == "on" else False

        if subject == "" or author == "" or body == "" or date == "":
            return render_template("write.html", errmsg="please fill out the blanks")
        
        if len(subject) > 50 or len(author) > 20 or len(body) > 400 or len(date) > 15:
            return render_template("write.html", errmsg="too long")

        try:
            assert write_data({"subject":subject, "author":author, "body":body, "secret":secret, "date":int(date)})==True
        except:
            abort(500)
        return redirect("/board")
    

@app.route("/reset", methods=["GET"])
def init():

    for file in os.listdir(f"{PATH}/db/metadata"):
        os.remove(f"{PATH}/db/metadata/{file}")
    for file in os.listdir(f"{PATH}/db/content"):
        os.remove(f"{PATH}/db/content/{file}")

    ts = int(datetime.now().timestamp() * 1000)
    write_data({"author":"guest",
                "secret":False,
                "date": ts-1000,
                "subject":"hi",
                "body":"hello world!"})
    write_data({"author":"admin",
                "secret":True,
                "date": ts,
                "subject":"FLAG",
                "body":"DH{********}"})
    return redirect("/board")
    

if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0", port=3333, threaded=True)