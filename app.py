from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("/app/output/house_price_model.pkl", "rb"))

app = Flask(__name__)

# HTML template for user input
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>House Price Prediction</title>
</head>
<body>
    <h1>House Price Prediction</h1>
    <form action="/predict-form" method="post">
        <label for="MedInc">Median Income (0-15):</label>
        <input type="number" step="any" name="MedInc" required><br>
        
        <label for="HouseAge">House Age (0-52):</label>
        <input type="number" step="any" name="HouseAge" required><br>

        <label for="AveRooms">Average Rooms (0-20):</label>
        <input type="number" step="any" name="AveRooms" required><br>

        <label for="AveBedrms">Average Bedrooms (0-10):</label>
        <input type="number" step="any" name="AveBedrms" required><br>

        <label for="Population">Population (0-40000):</label>
        <input type="number" step="any" name="Population" required><br>

        <label for="AveOccup">Average Occupancy (0-10):</label>
        <input type="number" step="any" name="AveOccup" required><br>

        <label for="Latitude">Latitude (32-42):</label>
        <input type="number" step="any" name="Latitude" required><br>

        <label for="Longitude">Longitude (-124 to -114):</label>
        <input type="number" step="any" name="Longitude" required><br>

        <input type="submit" value="Predict Price">
    </form>
</body>
</html>
"""

@app.route('/')
def form():
    return render_template_string(html_template)


@app.route('/predict-form', methods=['POST'])
def predict_form():
    try:
        # Extract features from form submission
        med_inc = float(request.form.get('MedInc'))
        house_age = float(request.form.get('HouseAge'))
        ave_rooms = float(request.form.get('AveRooms'))
        ave_bedrms = float(request.form.get('AveBedrms'))
        population = float(request.form.get('Population'))
        ave_occup = float(request.form.get('AveOccup'))
        latitude = float(request.form.get('Latitude'))
        longitude = float(request.form.get('Longitude'))

        # Validate the values
        features = [med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]

        # Make prediction
        features = np.array([features])
        prediction = model.predict(features)

        # Return the result in the web page
        return f"<h2>Predicted House Price: ${prediction[0]:.2f}</h2><br><a href='/'>Go Back</a>"

    except Exception as e:
        return f"<h2>Error: {str(e)}</h2><br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
