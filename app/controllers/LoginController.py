import re
from flask import render_template, request, redirect
from app import db
from app.models import Register
import requests
import json
from cryptography.hazmat.primitives import hashes



def login():
    #psycopg2.cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST': #and 'correo' in request.form and 'contrasena' in request.form:
        correo = request.form['correo']
        contrasena = request.form ['contrasena']
        print(contrasena)  
        #psycopg2.cursor.execute('SELECT * FROM registros WHERE correo = %s', (correo,))
        #account = psycopg2.cursor.fetchone()
        """
        if account:
            contrasena_rs = account['contrasena']
            print (contrasena_rs)
            if check_password_hash(contrasena_rs, 'admin'):
                session['loggedin'] = True
                session['id']= account['id']
                session['correo']= 'admin'
                return redirect(url_for('admin'))   

            elif check_password_hash(contrasena_rs, contrasena):
                session['loggedin']= True
                session['id']= account ['id']
                session['correo'] = account['correo']
                return redirect(url_for('usuario'))
            else:
                flash('Incorrect correo/contrasena') 
        else:
            flash('Incorrect correo/contrasena')
            
            
        if not correo or not contrasena:
            return "No hay parametros"
        """
        try:
            user = Register.query.filter(Register.correo == correo).first()
            if user == None or password != user.password:
                return "Invalid username or password"
            email = user.email
            password = bytes(password, 'utf-8')
            digest = hashes.Hash(hashes.SHA256())
            digest.update(password)
            hashedPassword = str(digest.finalize())
            return redirect("")
        except Exception as err:
            print(err)
            return "Error while accessing user. Try again"
                        
    return render_template('login.html')  