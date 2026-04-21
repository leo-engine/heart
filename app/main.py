from fastapi import FastAPI
from schemas.patient import PatientData
from model.predict import predict

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Heart Disease API"}

# @app.post("/predict")
# def make_prediction(data: PatientData):
#     result = predict(data)
#     return {"prediction": result}

