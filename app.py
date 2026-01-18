from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def dashboard():
    asset = request.form.get("asset")
    exposure = request.form.get("exposure")
    impact = request.form.get("impact")

    attacks = ["SQL Injection", "XSS", "Brute Force"]
    attack = random.choice(attacks)

    score = 40
    if exposure == "High":
        score += 25
    if impact == "High":
        score += 25

    risk_score = min(score, 95)

    risk_level = "High" if risk_score >= 75 else "Medium"
    color = "red" if risk_score >= 75 else "orange"

    explanation = "Simulated AI risk analysis based on exposure and impact."

    return render_template(
        "dashboard.html",
        asset=asset,
        exposure=exposure,
        impact=impact,
        attack=attack,
        score=risk_score,
        level=risk_level,
        color=color,
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)
