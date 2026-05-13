import subprocess
import pandas as pd
import numpy as np
import joblib
import re

# Load trained model and scaler
model = joblib.load("anomaly_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

print("\nStarting Kubernetes AI Monitor...\n")

# Get Kubernetes pod metrics
try:
    metrics_output = subprocess.check_output(
        ["kubectl", "top", "pods"],
        text=True
    )

except subprocess.CalledProcessError as e:
    print("Failed to fetch Kubernetes metrics.")
    print(e)
    exit(1)

# Split lines
lines = metrics_output.strip().split("\n")

# Skip header
pod_metrics = lines[1:]

anomaly_detected = False

for pod in pod_metrics:

    columns = pod.split()

    pod_name = columns[0]

    cpu_raw = columns[1]
    mem_raw = columns[2]

    # Convert CPU
    cpu_value = int(re.sub(r"[^0-9]", "", cpu_raw))

    # Convert Memory
    mem_value = int(re.sub(r"[^0-9]", "", mem_raw))

    # Create dataframe
    df = pd.DataFrame([{
        "cpu_usage": cpu_value,
        "memory_usage": mem_value
    }])

    # Scale metrics
    scaled = scaler.transform(df)

    # Predict anomaly
    prediction = model.predict(scaled)[0]

    if prediction == -1:

        anomaly_detected = True

        print(f"\n[ALERT] Anomaly detected in pod: {pod_name}")

        # Delete pod for self-healing
        print(f"[ACTION] Restarting pod: {pod_name}")

        subprocess.run([
            "kubectl",
            "delete",
            "pod",
            pod_name
        ])

if anomaly_detected:

    print("\n[ACTION] Scaling deployment to 5 replicas")

    subprocess.run([
        "kubectl",
        "scale",
        "deployment",
        "webapp",
        "--replicas=5"
    ])

else:
    print("\nNo anomalies detected. Cluster healthy.")

