from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Giri Babu", "Vani Kumari", "Tulasi Sai Priya", "Siva Durga Teja","Papi Reddy", "Alice", "Bob", "Charlie"]
    return render_template("index.html", names=names)