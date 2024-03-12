from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# Konfiguracja CORS
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/static/data', methods=['POST', 'OPTIONS'])  # Dodaj 'OPTIONS' do obsługi preflight
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])  # Dekorator cross_origin
def receive_data():
    data = request.json
    print(data)
    return jsonify({"message": "Dane zostały otrzymane i przetworzone"}), 200

if __name__ == '__main__':
    app.run(debug=True)
