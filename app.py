from flask import Flask, render_template, request

app = Flask(__name__)


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

        print("Nome:", name)
        print("E-mail:", email)
        print("Assunto:", subject)
        print("Mensagem:", message)

    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)