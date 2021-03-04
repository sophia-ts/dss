from flask import Flask, render_template, request, jsonify
from internal.utils.predict import predict
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def prediction():
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    chest_pain = int(request.form["chestPain"])
    resting_blood_pressure = int(request.form["restingBloodPressure"])
    serum_cholestoral = int(request.form["serumCholestoral"])
    fasting_blood_sugar = int(request.form["fastingBloodSugar"])
    if fasting_blood_sugar > 120:
        fasting_blood_sugar = 1
    else:
        fasting_blood_sugar = 0
    restingel_ectrocardiographic_results = int(
        request.form["restingelEctrocardiographicResults"]
    )
    maximum_heart_rate_achieved = int(request.form["maximumHeartRateAchieved"])
    exercise_induced_angina = int(request.form["exerciseInducedAngina"])
    oldpeak = float(request.form["oldpeak"])
    st_segment = int(request.form["stSegment"])
    number_of_vessels = int(request.form["numberOfVessels"])
    thal = int(request.form["thal"])

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

    return render_template("index.html", response=response)