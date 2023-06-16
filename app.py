
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

        # Perform prediction using the loaded model
        prediction = model.predict_proba([[input1, input2, input3, input4, input5]])
        # prediction = [1]
        # Prepare the prediction result for display
        result = f"The probability of heart failure is {round(prediction[0][1], 3)}"

        return jsonify(result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
