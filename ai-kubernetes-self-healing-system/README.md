# Kubernetes AI Self-Healing System

## Overview
This project demonstrates an AI-driven self-healing Kubernetes environment using Minikube, Python, and machine learning.

The system monitors Kubernetes pod resource metrics, detects anomalies using an Isolation Forest model, and automatically performs remediation actions such as restarting unhealthy pods and scaling deployments.

---

## Objectives

- Deploy a Kubernetes cluster locally using Minikube
- Deploy and scale containerized workloads
- Train an AI anomaly detection model
- Integrate AI monitoring with Kubernetes operations
- Automate pod healing and deployment scaling
- Demonstrate self-healing cloud-native infrastructure

---

## Technologies Used

- Kubernetes
- Minikube
- Docker
- Python 3
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Kubectl

---

## Project Components

### Kubernetes Deployment
- NGINX deployment
- NodePort service exposure
- Replica scaling

### AI Anomaly Detection
- Isolation Forest model
- CPU and memory anomaly detection
- Feature scaling with StandardScaler

### Self-Healing Automation
- Real-time Kubernetes metrics collection
- Automatic unhealthy pod deletion
- Automatic deployment scaling

---

## Key Skills Demonstrated

- Kubernetes administration
- Cloud-native workload orchestration
- AI-driven infrastructure monitoring
- Automated remediation workflows
- Python automation scripting
- Metrics-based anomaly detection
- Self-healing systems design

---

## Troubleshooting & Fixes

### Fixed outdated kubectl installation
Replaced deprecated Ubuntu package installation with the official Kubernetes repository installation method.

### Fixed scaler misuse during inference
Implemented production-correct ML preprocessing by saving and reusing the same scaler during prediction.

### Removed unnecessary TensorFlow dependency
TensorFlow was removed because the project uses Isolation Forest from scikit-learn only.

### Enabled metrics-server manually
Resolved missing Kubernetes Metrics API required for `kubectl top pods`.

### Improved realism of monitoring
Replaced simulated random metrics with live Kubernetes pod metrics using `kubectl top pods`.

---

## Future Improvements

- Prometheus integration
- Grafana dashboards
- Horizontal Pod Autoscaler (HPA)
- Real production telemetry training
- AlertManager integration
- Multi-node Kubernetes cluster support
