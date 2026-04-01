# module 11 - Flask Application
# Mia Maiers 3/31/2026

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html"
    )  # Render the index.html template when accessing the root URL


@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
