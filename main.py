from flask import *
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vamshi123',
    port='3306',
    database='cca_users'
)
global name

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html");


@app.route("/Next")
def Next():
    return render_template("Next.html")


@app.route("/savedetails", methods=["POST", "GET"])
def success():
    msg = "msg"
    if request.method == "POST":
        return render_template("success.html", msg=msg)


@app.route("/new")
def New():
    return render_template("new.html")


# @app.route("/success", methods=["POST", "GET"])
# def final():
#     msg = "msg"
#     if request.method == "POST":
#         return render_template("final.html", msg=msg)
#
#
@app.route("/final")
def back():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(port=3013)
