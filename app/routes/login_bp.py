from flask import Blueprint
from app.controllers.LoginController import login
login_bp = Blueprint('login_bp', _name_)

login_bp.route("/", methods=["GET", "POST"]) (Login)


