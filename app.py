from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from 2-Tier App with Docker Compose"

app.run(host="0.0.0.0", port=5000)
