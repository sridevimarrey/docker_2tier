from flask import Flask, render_template, request
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

# Show the form
@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    feedback = request.form.get("feedback")

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)",
            (name, email, feedback)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Database Error:", e)
        return "Error saving feedback", 500

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


