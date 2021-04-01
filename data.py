import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sqlite3
from app import db
from sqlalchemy import create_engine

countydf = pd.read_csv('..project_datasets/us-counties.csv', encoding="ISO-8859-1")

statesdf = pd.read_csv('..project_datasets/us-states.csv', encoding="ISO-8859-1")

engine = create_engine('sqlite:///uscoviddata.db', echo=True)
sqlite_connection = engine.connect()
countydf.to_sql('county', con=db.engine)
statesdf.to_sql('states', con=db.engine)
engine.execute("SELECT * FROM county").fetchall()
engine.execute("SELECT * FROM states").fetchall()

sqlite_connection.close()
