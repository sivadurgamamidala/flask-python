import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1

    #Method 1 
    # new_year = True --> this means we are telling to web application that it is new year today. So html content is able to change depending upon values of variables
    # new_year = True 
    return render_template("index.html", new_year=new_year)

    # Method 2
    # text = "Yes" if new_year else "No"
    # return render_template("index.html", new_year=text)
    #<h1>{{ new_year }}</h1> use this line of code in index.html

    # Method1 and Method2 results the same