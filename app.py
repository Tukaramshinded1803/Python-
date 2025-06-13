from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rm = float(request.form['rooms'])
    prediction = model.predict([[rm]])
    return render_template('index.html', prediction_text=f'Estimated Price: ${prediction[0]*1000:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
  
