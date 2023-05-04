import json
from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Register

def Register():
    
    if request.method == "POST":
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        try:
            user1 = Register.query.filter(Register.nombres == nombres).first()
            user2 = Register.query.filter(Register.correo == correo).first()
        except Exception as err:
            print(err)
            return "Error while accessing user. Try again"

        if user1 != None:
            return "Username already exists"
        if user2 != None:
            return "Email already exists"

        user = Register(nombres=nombres,correo = correo,contrasena = contrasena,apellidos= apellidos)
        #newPoints = Puntos(username=username,position = PuestoDefault(),corrects = 0,fails=0,points = 0)
        
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Internal server error. Try again later"
        return redirect("/login")
    return render_template("register.html")