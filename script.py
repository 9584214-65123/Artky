import psycopg2
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import( Flask, jsonify,
     redirect,
     render_template,
     request,
     url_for,
     flash,
     session)





DB_HOST = "localhost"
DB_NAME = "artky"
DB_USER = "postgres"
DB_PASS = "noemiinpostgrest"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=  'postgresql://postgres:noemiinpostgrest@localhost:5432/artky'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'cairocoders-ednalan'
migrate= Migrate(app,db)


#Modelo Register
class Register(db.Model):
    __tablename__= 'registros'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=True)
    apellidos = db.Column(db.String(50), nullable=True)
    correo = db.Column(db.String(50), nullable=True)
    contrasena = db.Column(db.String(50), nullable=True)
    

    def __repr__(self):
        return f'Register:{self.id},{self.nombres}, {self.apellidos}, {self.correo}, {self.contrasena}'

#Modelo Productos
class Catalogo(db.Model):
    __tablename__ = 'catalogos'
    id = db.Column(db.Integer, primary_key = True)
    producto = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    list_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable= False)

    def __repr__(self):
        return f'Catalogo:{self.id}, {self.producto}, {self.precio} '

#Modelo Categorias
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key = True)
    nombre_categoria = db.Column(db.String(50), nullable = False)
    catalogos = db.relationship('Catalogo', backref = 'list', lazy = True)

    def __repr__(self):
        return f'Categoria: {self.id}, {self.nombre_categoria}  '

db.create_all()
