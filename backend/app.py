import os
from flask import Flask
from db_access import get_db_connection

app = Flask(__name__)


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM test;")
        numbers = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return {"numbers": numbers}
