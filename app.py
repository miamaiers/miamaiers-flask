# module 11 - Flask Application
# Mia Maiers 3/31/2026

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
