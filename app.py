from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('label_encoders.pkl')

# Correct reverse map for output prediction
play_map_rev = {i: label for i, label in enumerate(encoders['Play'].classes_)}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            outlook = request.form['outlook']
            temp = request.form['temperature']
            humidity = request.form['humidity']
            wind = request.form['wind']

            # Encode input
            outlook_encoded = encoders['Outlook'].transform([outlook])[0]
            temp_encoded = encoders['Temperature'].transform([temp])[0]
            humidity_encoded = encoders['Humidity'].transform([humidity])[0]
            wind_encoded = encoders['Wind'].transform([wind])[0]

            features = [[outlook_encoded, temp_encoded, humidity_encoded, wind_encoded]]
            pred = model.predict(features)[0]
            prediction = play_map_rev.get(pred, "Unknown")

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
