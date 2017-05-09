from flask import Flask, request

app = Flask(__name__)


# Run this in a terminal:
# export FLASK_APP=server/api.py
# python3 -m flask run

@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
    content = request.get_json(silent=True)
    print(content)
