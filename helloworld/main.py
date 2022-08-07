from flask import Flask  
from flask import render_template
from flask import url_for
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500) # add app and parameters


@app.route("/")
def hello():  
    test = 'Test'
    return render_template('index.html', test=test)


@app.route("/home", methods=['GET'])
def home(): 
    return '<p>New page hello world example!!!</p>'


if __name__ == "__main__":
    # app.run() for debug
    ui.run()
   