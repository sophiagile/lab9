import sqlite3
import random 
from flask import Flask, session, render_template, request, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poems.db'  # Replace 'your_database.db' with the path to your SQLite database file
db = SQLAlchemy(app)
app.secret_key = "key1" 

@app.route("/")
def index():
    data = get_db()
    return str(data)

def get_db():
    db = getattr(g, 'database', None)
    if db is None: 
        db = g._database = sqlite3.connect('poems.db')
        cursor = db.cursor()
        cursor.execute("select * from poems")
    return cursor.fetchall()

@app.teardown_appcontext
def close_connect(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close() 

if __name__=='__main__':
    app.run()