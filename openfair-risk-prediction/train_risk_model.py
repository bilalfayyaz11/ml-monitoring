import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv("risk_data.csv")

X = df[["asset_value", "threat_event_frequency", "vulnerability", "impact"]]
y = df["historical_loss"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

plt.scatter(y_test, y_pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("Risk Prediction vs Actual Loss")
plt.savefig("risk_prediction.png")
print("Plot saved to risk_prediction.png")

import joblib
joblib.dump(model, "risk_model.pkl")
print("Model saved to risk_model.pkl")
