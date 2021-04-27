from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from kmpstringmatching import kmpstringmatching
from werkzeug.utils import secure_filename
import os
from flask_bootstrap import Bootstrap

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#bootstrap = Bootstrap(app)

@app.route('/')
def open():
    return render_template('open.html')

@app.route('/', methods=['GET', 'POST'])
def upload_all():
    if request.method == 'POST':
        name = request.form['name']
        #print(name)
        #print(kmpstringmatching(name,"IF2211"))
        return render_template('showmessage.html',name=name)

if __name__ == "__main__":
    app.run(threaded=True)