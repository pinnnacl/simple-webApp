from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Hardcoded sample data
sample_data = [
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Jane", "age": 30},
    {"id": 3, "name": "Bob", "age": 35}
]

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
