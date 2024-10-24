from flask import Flask
from models import db
from flask_cors import CORS
from routes.register import register_bp
from routes.login import login_bp
from flask_jwt_extended import JWTManager
from routes.protected import protected_bp
from routes.create_employee import employee_bp
from routes.positions import position_bp
from routes.recipes_route import recipe_bp
from routes.employee_name import employee_name_bp


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "DELETE", "PUT"]}})

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotpot.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'zX22fdgFh%553bVCrd1'

    jwt = JWTManager(app)
    db.init_app(app)

    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(protected_bp)
    app.register_blueprint(employee_name_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(recipe_bp)

    return app


# uwaga na produkcji na to!
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True)


# import os
# from flask import Flask
# from models import db
# from flask_cors import CORS
# from routes.register import register_bp
# from routes.login import login_bp
# from flask_jwt_extended import JWTManager
# from routes.protected import protected_bp
# from routes.create_employee import employee_bp
# from routes.positions import position_bp
# from routes.recipes_route import recipe_bp
# from routes.employee_name import employee_name_bp
# from dotenv import load_dotenv
# import pymysql

# load_dotenv()

# pymysql.install_as_MySQLdb()

# def create_app():
#     app = Flask(__name__)
#     CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "DELETE", "PUT"]}})

#     user = os.getenv('DB_USER')
#     password = os.getenv('DB_PASSWORD')
#     host = os.getenv('DB_HOST')
#     database = os.getenv('DB_NAME')

#     app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{password}@{host}/{database}'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['JWT_SECRET_KEY'] = 'zX22fdgFh%553bVCrd1'

#     jwt = JWTManager(app)
#     db.init_app(app)

#     app.register_blueprint(register_bp)
#     app.register_blueprint(login_bp)
#     app.register_blueprint(protected_bp)
#     app.register_blueprint(employee_name_bp)
#     app.register_blueprint(employee_bp)
#     app.register_blueprint(position_bp)
#     app.register_blueprint(recipe_bp)

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         # db.drop_all()
#         db.create_all()
#     app.run(debug=True)
