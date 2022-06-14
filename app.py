from flask import Flask, render_template
import formPY

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7k926bh6492moep0192b3t67rc510x'

@app.route("/")
def hello():
    formPY.generate_travel_tables()
    return render_template('index.html')
