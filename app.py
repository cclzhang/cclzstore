from distutils.log import debug
from flask import Flask, render_template
import sqlite3
from database import *
from helpers import *

app = Flask(__name__)
app.jinja_env.filters["cad"] = cad

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/garage')
def garage():
    # Connect to database
    con = sqlite3.connect("inventory.db")

    # Convert rows from tuple to dict
    con.row_factory = dict_factory

    # Fetch data from database
    db = con.cursor()
    db.execute("SELECT * FROM items")
    items = db.fetchall() 
    
    # Set HTML
    return render_template("garage.html", items=items)

@app.route('/writings')
def writings():
    # Connect to database
    con = sqlite3.connect("inventory.db")

    # Convert rows from tuple to dict
    con.row_factory = dict_factory

    # Fetch data from database
    db = con.cursor()
    db.execute("SELECT * FROM writings")
    writings = db.fetchall()

    # Set HTML
    return render_template("writings.html", writings=writings)

@app.route('/learn')
def learn():
    # Connect to database
    con = sqlite3.connect("inventory.db")

    # Convert rows from tuple to dict
    con.row_factory = dict_factory

    # Fetch data from database
    db = con.cursor()
    db.execute("SELECT * FROM lessons")
    lessons = db.fetchall()

    # Set HTML
    return render_template("learn.html", lessons=lessons)

# con.close()

if __name__ == '__main__':
    app.run(debug = True)
