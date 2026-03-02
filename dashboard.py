from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = sqlite3.connect("siem.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events ORDER BY id DESC LIMIT 100")
    events = c.fetchall()
    return render_template("dashboard.html", events=events)

app.run(debug=True)
