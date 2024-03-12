from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

db = SQLAlchemy()

@app.route('/static/data', methods=['POST', 'OPTIONS'])
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def receive_data():
    data = request.json
    print(data)
    return jsonify({"message": "Dane zostały otrzymane i przetworzone"}), 200

if __name__ == '__main__':
    app.run(debug=True)



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    with app.app_context():
        from .routes import auth_routes, data_routes
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(data_routes.data_bp)

    return app
