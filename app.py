from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world!"


@app.route("/api/v1.0/precipitation")
def date():
    return ""


@app.route("/api/v1.0/stations")
def stations():
    return ""


@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(
        {
            tobs = session.query(Measure.tobs).\
filter(Measure.station == "USC00519281").\
filter(Measure.date >= query_year).all()
        }
    )


if __name__ == "__main__":
    app.run(debug=True)