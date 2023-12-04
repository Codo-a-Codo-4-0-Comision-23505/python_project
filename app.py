from flask import Flask
from flask import jsonify
from flask import request
#from flaskext.mysql import MySQL
from funciones.clases import Persona
import pymysql.cursors

app = Flask(__name__)

# Una vez lograda la conexion.. 
#connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='12345Admin',
#                             database='data',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

#with connection:
#    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#        sql = "SELECT * FROM `compradores`" # dame todos los userszz
#        cursor.execute(sql)
        #cursor.fetchone()
#        for row in cursor:
#            print(row)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

#mysql = MySQL()
#mysql.init_app(app) # Si tuvieramos un archivo de configuracion, esta es la mejor opcion...

myPersona = Persona(400000, "Ale", 100)

@app.route("/hola")
def hello():
    return "<p>Hola, Mundo!</p>"

@app.route("/chau")
def bye():
    return "<p>chau, Mundo!</p>"

@app.route("/contacto", methods = ['POST', 'GET'])
def contactoHandling():
    respuesta = jsonify(myPersona.json)
    # Vamos a permitir conexion de cualquier lado ##WARNING! Security
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'POST':
        data = request.form
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345Admin',
                             database='data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `contacto` (`email`, `motivo`, `mensaje`) VALUES (%s, %s, %s)" # 
                cursor.execute(sql, (data['email'],data['motivo'], data['mensaje']))
            connection.commit()
        print(data['email'])
        print(data['motivo'])
        print(data['mensaje'])
    return respuesta

@app.route("/productos", methods = ['GET'])
def productosHandling():
    respuesta = jsonify([{'name': 'MS'}, {'name': 'GGle'}, {'name': 'IM'}])
    # Vamos a permitir conexion de cualquier lado ##WARNING! Security
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    
    return respuesta

@app.route("/compradores", methods = ['GET'])
def compradoresHandling():
    data = []
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345Admin',
                             database='data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `compradores`" # dame todos los userszz
            cursor.execute(sql)
            #cursor.fetchone()
            for row in cursor:
                data.append(row)
    
    respuesta = jsonify(data)
     # Vamos a permitir conexion de cualquier lado ##WARNING! Security
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta