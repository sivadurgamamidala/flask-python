from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World! this is shiva durga mamidala</h1>"

@app.route("/shiva")
def shiva():
    return "hello world! this is shiva"

@app.route("/tulasi")
def tulasi():
    return "welcome tulasi"

@app.route("/<string:name>")
def name(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"