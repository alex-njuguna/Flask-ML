import pickle
from flask import Flask, render_template, request


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    temperature = request.form.get("temperature")
    try:
        temperature = float(temperature)
        prediction = model.predict([[temperature]])
        output = round(prediction[0], 2)

        return render_template("index.html", prediction_text=f"Total expected revenue at a temperature of {temperature} is KeS {output}/-")
    except ValueError:
        return render_template("index.html", prediction_text="Please enter a valid temperature.")


if __name__ == "__main__":
    app.run(debug=True)