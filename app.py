from flask import Flask, render_template

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7k926bh6492moep0192b3t67rc510x'

@app.route("/")
def hello():
    print(__name__)
    return render_template('index.html')
