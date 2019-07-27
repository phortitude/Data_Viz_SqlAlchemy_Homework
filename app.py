# import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

print(Base.classes.keys())
# Save reference to the table
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)



# create an app, pass __name__
app = Flask(__name__)

# prcp_dict = {"date": "prcp"}
# stations = 
# Define what to do when a user hits the index route
@app.route("/")
def home():
#     print("Server received request for 'Home' page...")
    return (f"Welcome to my 'Climate Analysis' page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end><br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
        date_range = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        session = Session(engine)
        rain = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_range).all()
        session.close()
        
        return jsonify(rain)

@app.route("/api/v1.0/stations")
def stations():
        session = Session(engine)
        active_stations = session.query(Measurement.station)
        session.close()
        
        return jsonify(active_stations)
       
  

# # Define what to do when a user hits the /about route
# @app.route("/about")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)