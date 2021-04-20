from flask import Flask, render_template, request, jsonify
from internal.utils.predict import predict
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def prediction():
    age = int(request.json["age"])
    sex = int(request.json["sex"])
    chest_pain = int(request.json["chestPain"])
    resting_blood_pressure = int(request.json["restingBloodPressure"])
    serum_cholestoral = int(request.json["serumCholestoral"])
    fasting_blood_sugar = int(request.json["fastingBloodSugar"])
    if fasting_blood_sugar > 120:
        fasting_blood_sugar = 1
    else:
        fasting_blood_sugar = 0
    restingel_ectrocardiographic_results = int(
        request.json["restingelEctrocardiographicResults"]
    )
    maximum_heart_rate_achieved = int(request.json["maximumHeartRateAchieved"])
    exercise_induced_angina = int(request.json["exerciseInducedAngina"])
    oldpeak = float(request.json["oldpeak"])
    st_segment = int(request.json["stSegment"])
    number_of_vessels = int(request.json["numberOfVessels"])
    thal = int(request.json["thal"])

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

    return jsonify(response), 200