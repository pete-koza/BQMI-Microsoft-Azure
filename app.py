from flask import Flask, render_template
from dash import dcc, html, Input, Output, callback
from pages import formPY

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7k926bh6492moep0192b3t67rc510x'

@app.route("/")
def main():
    return html.Div('Hello')
