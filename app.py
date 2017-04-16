from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ingestion")
def ingestion():
    return render_template('ingestion.html')

@app.route("/exploration")
def exploration():
    return render_template('exploration.html')

@app.route("/learning")
def learning():
    return render_template('learning.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

