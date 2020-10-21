# PULL IN DEPENDENCIES AND MAKE CONNECTION
import sqlite3

conn = sqlite3.connect('?????.db')

from datetime import datetime

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# CREATE TABLE IF NEEDED

conn.execute("""CREATE TABLE IF NOT EXISTS air_sea_temps (
                latitude FLOAT,
                longitude FLOAT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                air_temperature FLOAT,    
                sea_surface_temp FLOAT     
                )""")

# # ADD VALUES IF NEEDED
# values = ('Deep Learning', 
#           'Ian Goodfellow et al.', 
#           775, 
#           datetime(2016, 11, 18).timestamp())

# #EXECUTE COMMAND
# conn.execute("""INSERT INTO books VALUES (?, ?, ?, ?)""", values)

#QUERY
r = conn.execute("""SELECT * FROM ?????""")
r.fetchall()