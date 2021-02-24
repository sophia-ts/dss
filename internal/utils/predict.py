import pickle
import os
import sklearn


def predict(data):
    # load the model
    path = os.getcwd() + "/internal/utils/"
    with open(path + "model.pkl", "rb") as model:
        classifier = pickle.load(model)

    prediction = classifier.predict(data)

    return prediction