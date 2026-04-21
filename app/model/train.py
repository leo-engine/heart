import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/heart.csv")

# clean column names
df.columns = df.columns.str.strip()

# target column (Kaggle dataset)
target_col = "target"

X = df.drop(target_col, axis=1)
y = df[target_col]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# save model
joblib.dump(model, "app/model/model.pkl")

print("Model trained successfully!")