<!-- # Naive-Bayes

<img width="889" height="743" alt="image" src="https://github.com/user-attachments/assets/78ae0187-671e-4e6b-b586-a1610f5af35d" />
 -->

## Naive Bayes Classifier – Student Pass Predictor

 This project implements a Naive Bayes classification model using Flask and scikit-learn. It predicts whether a student will pass or fail based on academic-related features provided by the user through a web interface.

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
├── student_data.csv         # Dataset used for training
├── templates/
│   └── index.html           # Frontend for input form
└── static/
    └── style.css            # (optional) Custom styles
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

## Screenshots

<img width="889" height="743" alt="image" src="https://github.com/user-attachments/assets/78ae0187-671e-4e6b-b586-a1610f5af35d" />

## Future Improvements

Auto-detect feature types for encoding

Add support for numeric features

Display prediction probability

Upload dataset for bulk prediction
