
import pandas as pd
from sklearn.model_selection  import train_test_split

df= pd.read_csv("data/heart.csv")
X=df.drop(["HeartDisease"],axis=1)
y=df["HeartDisease"]

Xtrain, Xtest, Ytrain, Ytest =train_test_split(X,y,test_size=0.2, random_state=42)



























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

