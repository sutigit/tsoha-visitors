from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = text("INSERT INTO visitors (time) VALUES (NOW())")
    db.session.execute(sql)
    db.session.commit()

    sql = text("SELECT COUNT(*) FROM visitors")
    result = db.session.execute(sql)
    counter = result.fetchone()[0]
    return render_template("index.html", counter=counter) 