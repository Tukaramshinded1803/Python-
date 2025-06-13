from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        rm = float(request.form['rooms'])
        prediction = model.predict([[rm]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f"Estimated Price: ${output * 1000}")
    except:
        return render_template('index.html', prediction_text="Invalid input.")

if __name__ == '__main__':
    app.run(debug=True)
  
