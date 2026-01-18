from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def dashboard():
    asset = "Web Application"

    attacks = ["SQL Injection", "XSS", "Brute Force"]
    attack = random.choice(attacks)

    risk_score = random.randint(60, 90)

    if risk_score >= 75:
        risk_level = "High"
        color = "red"
    elif risk_score >= 50:
        risk_level = "Medium"
        color = "orange"
    else:
        risk_level = "Low"
        color = "green"

    explanation = (
        "Exposure patterns detected based on simulated telemetry "
        "and asset criticality, indicating elevated attack likelihood."
    )

    return render_template(
        "dashboard.html",
        asset=asset,
        attack=attack,
        score=risk_score,
        level=risk_level,
        color=color,
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)
