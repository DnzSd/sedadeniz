import os
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("main.html")
    
if __name__ == "__main__":
    app.run()
