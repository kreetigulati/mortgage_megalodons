from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home Page')

@app.route("/prediction")
def prediction():
    return render_template('prediction.html', title='Prediction')

@app.route("/model")
def model():
    return render_template('model.html', title='Our Model')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

if __name__ == "__main__":
    app.run(debug=True)
