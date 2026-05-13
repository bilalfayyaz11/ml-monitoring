import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Reproducibility
np.random.seed(42)

# Simulated infrastructure metrics
data = {
    "cpu_usage": np.random.normal(50, 5, 1000),
    "memory_usage": np.random.normal(60, 10, 1000)
}

# Inject anomalies
data["cpu_usage"][200:250] = np.random.normal(90, 5, 50)
data["memory_usage"][400:450] = np.random.normal(20, 5, 50)

# Create DataFrame
df = pd.DataFrame(data)

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# Train anomaly detection model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(scaled_features)

# Predict anomalies
predictions = model.predict(scaled_features)

# Convert predictions
df["anomaly"] = [1 if x == -1 else 0 for x in predictions]

# Save artifacts
joblib.dump(model, "anomaly_detection_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel training completed successfully.\n")
print(df.head())
print("\nDetected anomalies:", df["anomaly"].sum())
