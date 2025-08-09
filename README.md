<!-- # Naive-Bayes

<img width="889" height="743" alt="image" src="https://github.com/user-attachments/assets/78ae0187-671e-4e6b-b586-a1610f5af35d" />
 -->

## Naive Bayes Classifier – Student Pass Predictor

 This project implements a Gaussian Naive Bayes classifier to predict whether an activity (e.g., playing tennis) will occur based on weather conditions.
It includes a simple Flask web interface for making predictions from user input.

## How It Works

- Uses LabelEncoder to encode string features

- Trains a Gaussian Naive Bayes classifier

- Saves both the model and the encoders for reuse

- Flask handles frontend rendering and backend prediction

---

## Project Structure

```
Naive-Bayes/
├── app.py                   # Flask app to serve predictions
├── train_model.py           # Naive Bayes training script
├── model.pkl                # Trained model file
├── encoders.pkl             # Label encoders for features and target
├── weather_play.csv          # Dataset used for training
├── templates/
│   └── index.html           # Frontend for input form

```

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Naive-Bayes.git
cd Naive-Bayes
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000

---
## Screenshots

### Step 1
<img width="1894" height="910" alt="image" src="https://github.com/user-attachments/assets/9be7769d-dbcb-40e8-808c-30376424d7b0" />

### Step 2
<img width="1894" height="900" alt="image" src="https://github.com/user-attachments/assets/786e4f96-e1d0-4ed6-8e9d-c704e3bcc1c2" />

### Step 3
<img width="1898" height="903" alt="image" src="https://github.com/user-attachments/assets/48629dd5-1899-4895-803f-3213074ea78d" />

---

## Future Improvements

Add more weather-related features.

Show prediction confidence/probabilities.

Provide batch prediction from CSV files.

Improve UI styling and responsiveness.
