from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Phase_2_Final_Project/project_datasets/us-counties.csv'

db = SQLAlchemy(app)

class USCounties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    county = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    cases = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)

class USStates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String, nullable=False)
    cases = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)

ButtonPressed = 0 
ButtonPressed2 = 0
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

def button():
    if requests.method == "POST":
        return render_template("home.html", ButtonPressed = ButtonPressed)
    return render_template("home.html", ButtonPressed = ButtonPressed)

    def button2():
        if requests.method == "POST":
            return render_template("home.html", ButtonPressed2 = ButtonPressed2)
        return render_template("home.html", ButtonPressed2 = ButtonPressed2)
    
    return render_template("home.html")

@app.route("/counties", methods=["GET"])
def counties():
    table = USCounties.query.all()
    d=[]

    for row in table:
        row_as_dict = {
            "date": row.date,
            "state": row.state,
            "county": row.county,
            "cases": row.cases,
            "deaths": row.deaths
        }
        d.append(row_as_dict)
    return jsonify(d)

@app.route("/states", methods=["GET"])
def states():
    table = USStates.query.all()
    d=[]

    for row in table:
        row_as_dict = {
            "date": row.date,
            "state": row.state,
            "cases": row.cases,
            "deaths": row.deaths
        }
        d.append(row_as_dict)
    return jsonify(d)

@app.route("/about", methods=["GET"])
def about():
    return """
    <!DOCTYPE html>
    <head>
        <title>About</title>
    </head>
    <body> 
        <h1> This database is a visualization of how different parts of the United States is handling COVID-19.</h1>
        <p> Over the course of the past year COVID-19 has ravaged the entire world.</p>
    </body>
        
    """

if __name__ == "__main__":
    app.run(debug=True)