# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traffic')
def traffic():
    return render_template('traffic.html')


# Omittable
if __name__ == "__main__":
    app.run(debug=True)


