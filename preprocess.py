import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load logs
log_file = "data/behavior_logs.csv"
df = pd.read_csv(log_file)

# Encode categorical features
le_user = LabelEncoder()
le_event = LabelEncoder()

df["user_encoded"] = le_user.fit_transform(df["user"])
df["event_encoded"] = le_event.fit_transform(df["event"])

# Save encoders for API use
os.makedirs("ml/encoders", exist_ok=True)
joblib.dump(le_user, "ml/encoders/le_user.pkl")
joblib.dump(le_event, "ml/encoders/le_event.pkl")

# Feature selection
X = df[["user_encoded", "event_encoded"]]
y = df["threat"]

# Save preprocessed data
X.to_csv("data/features.csv", index=False)
y.to_csv("data/labels.csv", index=False)

print("✅ Preprocessing complete. Encoders and features saved.")
