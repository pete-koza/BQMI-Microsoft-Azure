from flask import Flask, render_template
app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__app__':
    app.run(debug=True)