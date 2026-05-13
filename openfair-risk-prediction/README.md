# AI-Augmented Cybersecurity Risk Assessment Using OpenFAIR and Random Forest

## Objectives
- Simulate historical security incident data using the OpenFAIR risk quantification framework
- Train a Random Forest regression model to predict financial loss from threat scenarios
- Serialize and reload the trained model for reusable inference
- Visualize predicted risk distributions across multiple simulated scenarios

## Tools & Technologies
| Tool | Purpose |
|---|---|
| Python 3 | Core scripting language |
| pandas | Dataset creation and manipulation |
| NumPy | Synthetic data generation |
| scikit-learn | Random Forest Regressor, train/test split, MSE evaluation |
| matplotlib | Scatter plot and histogram visualization |
| joblib | Model serialization and reloading |
| OpenFAIR | Risk quantification methodology (Asset Value × TEF × Vulnerability × Impact) |

## Key Skills Demonstrated
- Applied OpenFAIR risk factors as structured ML features for financial loss prediction
- Built and evaluated a Random Forest regression pipeline with MSE scoring
- Solved cross-script model persistence using joblib serialization
- Resolved headless environment rendering issues via matplotlib Agg backend
- End-to-end ML workflow: data generation → training → inference → visualization

## Troubleshooting Log
| Issue | Root Cause | Fix Applied |
|---|---|---|
| `pip install` fails | Ubuntu 24.04 PEP 668 restriction | Added `--break-system-packages` flag |
| `plt.show()` hangs | No display in headless terminal | Replaced with `plt.savefig()` + `matplotlib.use('Agg')` |
| `NameError: model` in predict_risk.py | Model object not persistent across Python processes | Saved model with `joblib.dump()`, loaded with `joblib.load()` |
| `NameError: np` in visualize_risk.py | Missing numpy import in standalone script | Added explicit `import numpy as np` |

## Output Files
- `risk_data.csv` — Simulated OpenFAIR dataset (100 records)
- `risk_model.pkl` — Serialized trained Random Forest model
- `risk_prediction.png` — Actual vs predicted loss scatter plot
- `risk_distribution.png` — Histogram of predicted losses across 50 scenarios
