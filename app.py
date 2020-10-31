from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

@app.route("/")
def welcome():
     """List all available api routes."""
    return ()
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"

@app.route("/api/v1.0/precipitation")
def precipitation():
    query_year = dt.date(2017,8,23) - dt.timedelta(days = 365)
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= query_year).\
                order_by(Measurement.date).all()
    prcp_data_list = dict(prcp_data)
    return jsonify(prcp_data_list)


@app.route("/api/v1.0/stations")
def stations():
        stations = session.query(func.count(Station.station))
        station_count = stations[0]
        return jsonify(station_count)


@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(
        {
            tobs = session.query(Measure.tobs).\
filter(Measure.station == "USC00519281").\
filter(Measure.date >= query_year).all()
        }
    )


@app.route("/api/v1.0/<start>")
def start_day(start):
        start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                group_by(Measurement.date).all(
        start_day_list = list(start_day)
        return jsonify(start_day_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start, end):
        start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).\
                group_by(Measurement.date).all(
        start_end_day_list = list(start_end_day)
        return jsonify(start_end_day_list)

if __name__ == "__main__":
    app.run(debug=True)
