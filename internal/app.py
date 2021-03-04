from flask import Flask, render_template, request, jsonify
from internal.utils.predict import predict
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def prediction():
    age = request.form["age"]
    sex = request.form["sex"]
    chest_pain = request.form["chestPain"]
    resting_blood_pressure = request.form["restingBloodPressure"]
    serum_cholestoral = request.form["serumCholestoral"]
    fasting_blood_sugar = request.form["fastingBloodSugar"]
    restingel_ectrocardiographic_results = request.form[
        "restingelEctrocardiographicResults"
    ]
    maximum_heart_rate_achieved = request.form["maximumHeartRateAchieved"]
    exercise_induced_angina = request.form["exerciseInducedAngina"]
    oldpeak = request.form["oldpeak"]
    st_segment = request.form["stSegment"]
    number_of_vessels = request.form["numberOfVessels"]
    thal = request.form["thal"]

    data = [
        [
            age,
            sex,
            chest_pain,
            resting_blood_pressure,
            serum_cholestoral,
            fasting_blood_sugar,
            restingel_ectrocardiographic_results,
            maximum_heart_rate_achieved,
            exercise_induced_angina,
            oldpeak,
            st_segment,
            number_of_vessels,
            thal,
        ]
    ]

    data = np.array(data)

    prediction = predict(data)

    if prediction == [0]:
        response = "Low chance "
    else:
        response = "High chance "

    return jsonify(response)