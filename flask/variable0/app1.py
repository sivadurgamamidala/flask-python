from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "hello world! this is shiva"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Good Bye"
    return render_template("index.html", headline=headline)