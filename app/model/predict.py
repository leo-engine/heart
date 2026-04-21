import joblib
import numpy as np

model = joblib.load("model/model.pkl")

def predict(data):
    input_data = np.array([[
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]])

    return int(model.predict(input_data)[0])