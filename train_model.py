import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
import joblib

# Load dataset
data = pd.read_csv('weather_play.csv')

# Label encode all categorical columns
label_encoders = {}
for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Features and target
X = data[['Outlook', 'Temperature', 'Humidity', 'Wind']]
y = data['Play']

# Train Naive Bayes model
model = CategoricalNB()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Model and encoders saved successfully.")
