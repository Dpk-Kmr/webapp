
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('ABC_best.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the user inputs from the form
        input1 = float(request.form['input1'])
        input2 = float(request.form['input2'])
        input3 = float(request.form['input3'])
        input4 = float(request.form['input4'])
        input5 = float(request.form['input5'])

        if int(input1) != 0 and int(input1) != 1:
            result = "Kindly check the gender input again. It should be either 0 or 1."
        elif int(input2) != 0 and int(input2) != 1:
            result = "Kindly check the diabetes input again. It should be either 0 or 1."
        elif int(input3) < 50 or int(input3) > 200:
            result = "Kindly check the systolic blood pressure input again. It should be between 50 and 200 only."
        elif int(input4) < 40 or int(input4) > 200:
            result = "Kindly check the heart rate input again. It should be between 40 and 200 only."
        elif int(input5) < 120 or int(input5) > 145:
            result = "Kindly check the sodium level input again. It should be between 120 and 145 only."
        else:    
            # Perform prediction using the loaded model
            prediction = model.predict_proba([[input1, input2, input3, input4, input5]])
            # prediction = [1]
            # Prepare the prediction result for display
            result = f"Prediction result: The probability of heart failure is {round(prediction[0][1], 3)}"

        return jsonify(result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
