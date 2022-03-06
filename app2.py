from distutils.log import debug
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello():
    return 'asdfasdf'#render_template("garage.html")

@app.route('/garage')
def hello1():
    return render_template("garage.html")

@app.route('/writings')
def hello2():
    return render_template("writings.html")

@app.route('/learn')
def hello3():
    return render_template("learn.html")


if __name__ == "__main__":
    app.run(debug=True)
