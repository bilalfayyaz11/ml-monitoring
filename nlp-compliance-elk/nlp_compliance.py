import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

with open("logs/system.log", "r") as f:
    logs = f.readlines()

data = []
for line in logs:
    timestamp = re.search(r"\[(.*?)\]", line).group(1)
    level = re.search(r"\] (\w+):", line).group(1)
    message = re.search(r": (.*)", line).group(1)
    data.append((timestamp, level, message))

df = pd.DataFrame(data, columns=["timestamp", "level", "message"])

sia = SentimentIntensityAnalyzer()
df["sentiment"] = df["message"].apply(lambda x: sia.polarity_scores(x)["compound"])

df["compliance_risk"] = df["sentiment"] < -0.2
print(df[["timestamp", "level", "message", "compliance_risk"]])

df.to_csv("compliance_report.csv", index=False)
print("\n✅ Compliance report generated: compliance_report.csv")
