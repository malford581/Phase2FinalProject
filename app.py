from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def home():
    

if __name__ == "__main__":
    app.run(debug=True)