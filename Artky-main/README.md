# Artky (Artisan-community)

Integrantes:
- Mayra Medrano
- Junior Haro
- Yamileth Rincón
- Alvaro Herrera

# Descripción:
- Somos un grupo de estudiantes de UTEC que a través de "Artky" busca reivindicar la artesanía peruana, a través de un espacio que difunde las creaciones de nuestros artesanos asociados. En la página podrás encontrar el catálogo de artesanías de los miembros de nuestra comunidad.				

- La idea del proyecto nace a raíz de la pandemia cuando miles de artesanos sufieron pérdidas monetarias debido al confinamiento
De esta manera, queremos ayudar con un granito de arena a la comunidad de artesanos peruanos.

# Objetivos:

Objetivos principales:
- Impulsar el trabajo de los artesanos asociados
- Inspirar a nuevos artesanos
- Satisfacer las principales necesidades de nuestros usuarios

Misión:
- Promover la artesanía peruana a través de medios digitales

Visión:
- Ser el principal medio de difusión digital de artesanía en Perú

# Información acerca de las librerías/frameworks/plugins utilizadas en Front End, Back End y base de datos.

Librerías:
- SQLAlchemy:<br>
  Proporciona un conjunto completo de patrones diseñados para un acceso a bases de datos eficiente y de alto rendimiento.<br>
- redirect:<br>
  Un redirect (abreviatura de redirección) es un reenvío automático del lado del servidor o del cliente de una URL a otra. Se usa para la reubicación de un sitio web     en un nuevo dominio o el mantenimiento de un servidor.<br>
- render_template:<br>
  Recibe como parámetro el fichero donde guardamos la plantilla y las variables que se pasan a esta.<br>
- request:<br>
  Permite el acceso a toda la información que pasa desde el navegador del cliente al servidor.<br>
- Url_for:<br>
  Se usa para crear una URL para evitar la sobrecarga de tener que cambiar las URL en toda la aplicación.<br>
- Flask:<br>
  Micro framework escrito en Python y desarrollado para simplificar y hacer más fácil la creación de aplicaciones web.<br>
- register:<br>
  Sirve al compilador para indicarle que "intente" almacenar ese valor en un registro de la CPU en vez de directamente en memoria.<br>
- Check:<br>
  Especifica los valores que acepta un campo, evitando que se ingresen valores inapropiados cuando ejecutamos un comando insert o update.<br>
- Response:<br>
  Sirve para presentar en la pantalla del navegador del cliente el resultado de cualquier código que hayamos escrito.<br>
- Cursor:<br>
  Se utiliza para el procesamiento individual de las filas devueltas por el sistema gestor de base de datos para una consulta.<br>
- Werkzeug.security:<br>
  Esta libreria basicamente la hemos usado para hashear la contraseña.<br>
- Flask_Migrate<br>
- Psycopg2<br>

Frameworks:
- JS -> Java Script 
- Python
- Flask

Database:
- Postgresql

# Nombre del script a ejecutar para iniciar la base de datos con datos.
- app.py

# Información acerca de los API.Requests y Responses de cada endpoint utilizado en el sistema.
- API.Requests: 
  Usamos varios @app.route que reciben y retornan la información entre servidor y cliente.
  
- Response:<br>
 @app.route('/register/registrar', methods= ['POST']  )<br>
 def resgistrar():<br>
     try:<br>
        nombres = request.get_json()['nombres']<br>
        apellidos = request.get_json()['apellidos']<br>
        correo = request.get_json()['correo']<br>
        contrasena = request.get_json()['contrasena']<br>
        registro = Register (nombres=nombres, apellidos=apellidos, correo=correo, contrasena=contrasena)<br>
        db.session.add(registro)<br>
        db.session.commit()<br>
    except:<br>
        db.session.rollback()<br>
        error = True<br>
    finally:<br>
        return render_template("register.html", error = error)<br>
        
- Endpoints
  - '/' index
  - '/home': Muestra la página principal de la aplicación con los botones Log in, Sign up y Settings.
  - '/register': Pagina para registrarse
  - '/login': Iniciar sesión

# Hosts.
- localhost = 5432 
- Port = 5000

# Forma de autenticación.
- Para la autenticación de los usuarios decidimos usar lenguaje SQL.

# Manejo de errores HTTP:<br>
  500: Errores en el servidor<br>
  400: Errores en el Cliente<br>
  300: Redirección<br>
  200: Exitoso<br>
  100: Informacional<br>
  
Manejo de errores:
- Los errores dentro de registrarse en la pagina web se manejan gracias a los "types" que verifican que un correo es ingresado correctamente.

@app.route('/register/registrar', methods= ['POST']  ) <br>
def resgistrar(): <br>
    try: <br>
        nombres = request.get_json()['nombres'] <br>
        apellidos = request.get_json()['apellidos'] <br>
        correo = request.get_json()['correo'] <br>
        contrasena = request.get_json()['contrasena'] <br>
        registro = Register (nombres=nombres, apellidos=apellidos, correo=correo, contrasena=contrasena) <br>
        db.session.add(registro) <br>
        db.session.commit() <br>
        error=False <br>
    except: <br>
        db.session.rollback() <br>
        error= True <br>
    finally: <br>
        db.session.close() <br>
        return render_template('success', error=error) <br>
  
# Cómo ejecutar el sistema (Deployment scripts)
 - Lo primero que debemos hacer es ejecutar el archivo "script.py" para la creación de la tabla en la base de datos y luego ejecutar el archivo "app.py" para levantar el servidor.
