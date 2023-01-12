from flask import Flask
from flask_jwt_extended import JWTManager
import uvicorn
from api.routes import *

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
