from flask import Flask


app = Flask(__name__)


@app.route("/")
def SendMessage():
    return "Hey i am Skynet"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
