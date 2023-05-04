from sqlalchemy import PrimaryKeyConstraint
 
from app import db


#Modelo Usuarios
class Register(db.Model):
    #__tablename__= 'registros'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)
    

    #def __repr__(self):
     #   return f'Register:{self.id},{self.nombres}, {self.apellidos}, {self.correo}, {self.contrasena}'
#Modelo Productos
class Catalogo(db.Model):
    #__tablename__ = 'catalogos'
    id = db.Column(db.Integer, primary_key = True)
    producto = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    list_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable= False)

    #def __repr__(self):
     #   return f'Catalogo:{self.id}, {self.producto}, {self.precio} '
#Modelo Categorias
class Categoria(db.Model):
    #__tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key = True)
    nombre_categoria = db.Column(db.String(50), nullable = False)
    catalogos = db.relationship('Catalogo', backref = 'list', lazy = True)

    #def __repr__(self):
     #   return f'Categoria: {self.id}, {self.nombre_categoria}  '
    
db.create_all()