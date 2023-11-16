from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello():
    return "<p>Hola, Mundo!</p>"


@app.route("/chau")
def bye():
    return "<p>chau, Mundo!</p>"