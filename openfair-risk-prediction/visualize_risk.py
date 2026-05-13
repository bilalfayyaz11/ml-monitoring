import pandas as pd
import numpy as np
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

model = joblib.load("risk_model.pkl")

new_scenarios = pd.DataFrame({
    "asset_value": np.random.uniform(1000, 5000, 50),
    "threat_event_frequency": np.random.uniform(0.1, 1.0, 50),
    "vulnerability": np.random.uniform(0.1, 1.0, 50),
    "impact": np.random.uniform(100, 1000, 50)
})

predicted_losses = model.predict(new_scenarios)

plt.hist(predicted_losses, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Predicted Loss ($)")
plt.ylabel("Frequency")
plt.title("Distribution of Predicted Risk Losses")
plt.savefig("risk_distribution.png")
print("Visualization saved to risk_distribution.png")
