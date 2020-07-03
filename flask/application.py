from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# to switch flask to application.py then use below command
# $env:FLASK_APP = "application.py" 
# > flask run