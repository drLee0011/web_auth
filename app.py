from flask import Flask
from flask_jwt_extended import JWTManager
from routes import app as routes_app

app = Flask(__name__)
app.secret_key = '599f144a68fd1342c0ab0317fe01c125'  # our secret key

# JWT configuration
app.config['JWT_SECRET_KEY'] = '599f144a68fd1342c0ab0317fe01c125'  # our secret key 
jwt = JWTManager(app)

# Register the blueprint
app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True)
