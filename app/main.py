from fastapi import FastAPI
from app.schemas.patient import PatientData
from app.model.predict import predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Heart Disease API"}

@app.post("/predict")
def make_prediction(data: PatientData):
    result = predict(data)
    return {"prediction": result}


























# print("---------------")
# print(df.shape)
print("---------------")
# print(Xtrain.shape)
# print(Xtest.shape)
# print("---------------")
# print(Ytrain.size)
# print(Ytest.size)

# print(df.isnull().sum())
# print("---------------")
# print(df.isnull().sum()[df.isnull().sum() > 0])

