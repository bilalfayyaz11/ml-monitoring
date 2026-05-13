import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "asset_value": np.random.uniform(1000, 5000, 100),
    "threat_event_frequency": np.random.uniform(0.1, 1.0, 100),
    "vulnerability": np.random.uniform(0.1, 1.0, 100),
    "impact": np.random.uniform(100, 1000, 100),
    "historical_loss": np.random.uniform(500, 3000, 100)
}

df = pd.DataFrame(data)
print(df.head())
df.to_csv("risk_data.csv", index=False)
print("Dataset saved to risk_data.csv")
