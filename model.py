import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load preprocessed data
X = pd.read_csv("data/features.csv")
y = pd.read_csv("data/labels.csv").values.ravel()

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
os.makedirs("ml", exist_ok=True)
joblib.dump(model, "ml/model.pkl")

print("✅ Model trained and saved as 'ml/model.pkl'")
