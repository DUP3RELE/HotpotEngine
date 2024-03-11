from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000/"}})

@app.route('/static/data', methods=['POST'])
def receive_data():
    data = request.json  # Pobierz dane JSON z zapytania
    print(data)  # Wyświetl dane w konsoli serwera
    # Tutaj możesz dodać logikę przetwarzania danych
    return jsonify({"message": "Dane zostały otrzymane i przetworzone"}), 200

if __name__ == '__main__':
    app.run(debug=True)