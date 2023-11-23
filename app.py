from flask import Flask
from funciones.clases import Persona

app = Flask(__name__)
myPersona = Persona(400000, "Ale", 100)

@app.route("/hola")
def hello():
    return "<p>Hola, Mundo!</p>"

@app.route("/chau")
def bye():
    return "<p>chau, Mundo!</p>"

@app.route("/contacto")
def contactoHandling():
    return myPersona.json