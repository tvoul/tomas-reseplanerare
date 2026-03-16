from flask import Flask, render_template, request
from backend import get_departures

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    departures = []

    if request.method == "POST":

        line = request.form["line"]
        direction = request.form["direction"]

        departures = get_departures(line, direction)

    return render_template("index.html", departures=departures)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
