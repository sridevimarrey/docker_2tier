from flask import Flask, render_template, request

app = Flask(__name__)

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

    # For now, just print (later we save to RDS)
    print("Name:", name)
    print("Email:", email)
    print("Feedback:", feedback)

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

