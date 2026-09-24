import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    return connection


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts", methods=["GET", "POST"])
def contacts():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO contact (
                name,
                email,
                subject,
                message
            )
            VALUES (?, ?, ?, ?)
            """,
            (name, email, subject, message)
        )

        connection.commit()
        connection.close()

    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)