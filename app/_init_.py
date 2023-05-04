from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

app = Flask(_name_)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models, topRoutes

from app.routes.login_bp import login_bp
from app.routes.register_bp import register_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(register_bp, url_prefix="/register")


db.create_all() # Create sql tables for our data models (Usuario and Score)