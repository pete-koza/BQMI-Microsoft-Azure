from flask import Flask, render_template
from dash import dcc, html, Input, Output, callback


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")
