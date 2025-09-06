import pandas as pd
import random
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import os
import joblib

# Create folders if not exist
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

# 1. Generate sample logs
rows = []
start = datetime.now()

for i in range(200):
    ts = start + timedelta(seconds=i*5)
    latency = random.gauss(100, 20)
    status = 200
    # inject anomalies (5% of logs)
    if random.random() < 0.05:
        latency = random.uniform(1000, 3000)
        status = 500
    rows.append([ts, latency, status])

df = pd.DataFrame(rows, columns=["timestamp", "latency_ms", "status"])

# 2. Train anomaly detector
X = df[["latency_ms", "status"]]
clf = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = clf.fit_predict(X)

# 3. Save logs
df.to_csv("data/logs_with_anomalies.csv", index=False)
print("Logs saved to data/logs_with_anomalies.csv")

# 4. Save model
joblib.dump(clf, "models/model.joblib")
print("Model saved to models/model.joblib")

# 5. Plot results
plt.figure(figsize=(10,5))
normal = df[df["anomaly"] == 1]
anomaly = df[df["anomaly"] == -1]

plt.scatter(normal["timestamp"], normal["latency_ms"], c="blue", label="Normal")
plt.scatter(anomaly["timestamp"], anomaly["latency_ms"], c="red", label="Anomaly")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.title("Log Anomaly Detection")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/anomalies_plot.png")
plt.show()

# your existing code
print("Logs saved...")
print("Model saved...")

# Keep container alive
import time
while True:
    time.sleep(60)

