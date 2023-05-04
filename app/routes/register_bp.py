from flask import Blueprint

from app.controllers.RegisterController import Register
register_bp = Blueprint('register_bp', _name_)

register_bp.route("/", methods=["GET", "POST"]) (Register)
